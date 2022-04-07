extends TileMap
class_name TemplateMaze

var maze_template = [
	["#", "#", "#", "#", "#", "S", "#"],
	["#", "E", " ", " ", "#", " ", "#"],
	["#", " ", "#", " ", "#", " ", "#"],
	["#", " ", "#", " ", " ", " ", "#"],
	["#", " ", "#", "#", "#", " ", "#"],
	["#", " ", " ", " ", " ", " ", "#"],
	["#", "#", "#", "#", "#", "#", "#"]
]

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

var nodes = []
var start_node_idx = null
var end_node_idx = null

signal updated

func _ready():
	_init_map()
	_center_map()

func _init_map():
	for y in range(len(maze_template)):
		for x in range(len(maze_template[0])):
			var maze_cell_symbol = maze_template[y][x]
			# isometric view requires x to be inverted
			var node = Vector2(-x, y)
			if maze_cell_symbol == Constants.START_CHAR:
				start_node_idx = get_node_index(node)
			if maze_cell_symbol == Constants.END_CHAR:
				end_node_idx = get_node_index(node)
			set_cell(y, -x, Constants.tile_mapping[maze_cell_symbol])
			nodes.append(node)
	emit_signal("updated")

func _center_map():
	var map_rect_pos = get_used_rect().end - Vector2(1, 0)
	transform.origin = get_viewport().size / 2 - map_rect_pos * cell_size / 2

func get_node_index(node: Vector2):
	"""Takes as input the coordinates of a node and returns its index.

	Args:
		node (Vector2): Node coordinates relative to the maze.

	Returns:
		node_idx (int): Index of the node relative to the maze.
	"""
	var maze_width = len(maze_template[0])
	return node.y * maze_width + node.x * -1

func get_node_symbol_by_idx(node_idx: int):
	"""Takes as input the index of a node and returns its symbol.

	Args:
		node_idx (int): Node index relative to the maze.

	Returns:
		node_symbol (str): Symbol denoting the type of node.
	"""
	var maze_width = len(maze_template[0])
	var i = node_idx / maze_width
	var j = node_idx % maze_width
	return maze_template[i][j]

func draw_path(path, open_interval=false):
	if open_interval:
		path.pop_back()
		path.pop_front()
	
	for tile in path:
		set_cell(tile.y, tile.x, 17)
		yield(get_tree(), "idle_frame")
	
	for tile in path:
		var current_tile = _coordinate_sum()
		for dir in road_connections:
			if get_cellv(Vector2(tile.y, tile.x) + dir) != _coordinate_sum():
				if get_cellv(Vector2(tile.y, tile.x) + dir) != 16:
					current_tile -= road_connections[dir]
		set_cellv(Vector2(tile.y, tile.x), current_tile)

func _coordinate_sum():
	return coordinates.N|coordinates.E|coordinates.S|coordinates.W
