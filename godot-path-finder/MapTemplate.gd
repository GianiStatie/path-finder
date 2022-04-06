extends TileMap

var maze = [
	["#", "#", "#", "#", "#", "O", "#"],
	["#", " ", " ", " ", "#", " ", "#"],
	["#", " ", "#", " ", "#", " ", "#"],
	["X", " ", "#", " ", " ", " ", "#"],
	["#", " ", "#", "#", "#", " ", "#"],
	["#", " ", " ", " ", " ", " ", "#"],
	["#", "#", "#", "#", "#", "#", "#"]
]

var tile_mapping = {
	" ": 15,
	"#": 16,
	"O": 17,
	"X": 17,
}

var weight_mapping = {
	15: 1,
	16: 999,
	17: 1
}

# Path draw variables
const coordinates = {
	'N': 1, 
	'E': 2,
	'S': 4,
	'W': 8
}

const road_connections = {
	Vector2(0,  1): coordinates.N, Vector2(-1, 0): coordinates.E,
	Vector2(0, -1): coordinates.S, Vector2( 1, 0): coordinates.W
}
const empty_road_tile = 16
const road_construction_tile = 17

#onready var astar = AStar2D.new()
onready var astar = BFS_Pathfinder.new()

var used_cells: Array
var path: PoolVector2Array
var start_node: Vector2
var end_node: Vector2

func _ready():
	_init_map()
	_center_map()
	_add_points()
	_connect_points()
	_get_path(start_node, end_node)
	draw_path()

func get_cell_id(cell_pos: Vector2) -> int:
	return used_cells.find(cell_pos, 0)

func get_cell_sybol_by_id(cell_id: int):
	var maze_height = len(maze)
	var y = int(cell_id / maze_height)
	var x = int(cell_id % maze_height)

func draw_path():
	for tile in path:
		set_cell(tile.x, tile.y, road_construction_tile)
		yield(get_tree(), "idle_frame")
		
	for tile in path:
		var current_tile = _coordinate_sum()
		for dir in road_connections:
			if get_cellv(Vector2(tile.x, tile.y) + dir) != _coordinate_sum():
				if get_cellv(Vector2(tile.x, tile.y) + dir) != empty_road_tile:
					current_tile -= road_connections[dir]
		set_cellv(Vector2(tile.x, tile.y), current_tile)

func _init_map():
	for i in range(len(maze)):
		for j in range(len(maze[0])):
			var maze_cell_symbol = maze[i][j]
			set_cell(i, -j, tile_mapping[maze_cell_symbol])
			if maze_cell_symbol == 'O': start_node = Vector2(i, -j)
			if maze_cell_symbol == 'X': end_node = Vector2(i, -j)
			used_cells.append(Vector2(i, -j))

func _center_map():
	var map_rect_pos = get_used_rect().end - Vector2(1, 0)
	transform.origin = get_viewport().size / 2 - map_rect_pos * cell_size / 2

func _add_points():
	for cell in used_cells:
		var cell_weight = weight_mapping[get_cellv(cell)]
		astar.add_point(get_cell_id(cell), cell, cell_weight)

func _connect_points():
	for cell in used_cells:
		for neighbor_direction in [Vector2.UP, Vector2.DOWN, Vector2.LEFT, Vector2.RIGHT]:
			var neighbor_cell = cell + neighbor_direction
			if used_cells.has(neighbor_cell):
				astar.connect_points(get_cell_id(cell), get_cell_id(neighbor_cell))

func _get_path(start, end):
	path = astar.get_point_path(get_cell_id(start), get_cell_id(end))
	## optional: remove start and end blocks
	# path.remove(0)
	# path.remove(path.size() - 1)

func _coordinate_sum():
	return coordinates.N|coordinates.E|coordinates.S|coordinates.W
