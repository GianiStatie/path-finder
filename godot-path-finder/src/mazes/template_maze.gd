extends TileMap
class_name TemplateMaze

var maze_template = [
	["#", "#", "#", "#", "#", "S", "#"],
	["#", " ", " ", " ", "#", " ", "#"],
	["#", " ", "#", " ", "#", " ", "#"],
	["E", " ", "#", " ", " ", " ", "#"],
	["#", " ", "#", "#", "#", " ", "#"],
	["#", " ", " ", " ", " ", " ", "#"],
	["#", "#", "#", "#", "#", "#", "#"]
]

var nodes = []
var start_node = null
var end_node = null

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
				start_node = get_node_index(node)
			if maze_cell_symbol == Constants.END_CHAR:
				end_node = get_node_index(node)
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
	return node[1] * maze_width + node[0] * -1

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
