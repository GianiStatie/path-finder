extends Node

var nodes = {}
var connections = {}
var obstacle_weight = Constants.weight_mapping[Constants.OBSTACLE_CHAR]

export(NodePath) onready var maze = get_node(maze) as TemplateMaze

func add_node(idx: String, position: Vector2, weight: float = 1.0):
	"""Adds node to the internal graph-like structure which describes the maze.

	Args:
		idx (int): Index of the node relative to the maze.
		position (Vector2): Coordinates of the node relative to the maze.
		weight (float, optional): Weight of the node denoted by its symbol. Defaults to 1.0.
	"""
	nodes[idx] = {
		"position": position,
		"weight": weight
	}

func connect_nodes(idx: String, to_idx: String, bidirectional: bool = true):
	"""Adds a connection between two nodes in the internal graph-like structure.

	Args:
		idx (int): Index of the parent node.
		to_idx (int): Index of the child node.
		bidirectional (bool, optional): Whether the child is also connected to the parent.
			Defaults to True.
	"""
	_add_connection(idx, to_idx)
	if bidirectional:
		_add_connection(to_idx, idx)

func _add_nodes():
	for node_idx in len(maze.nodes):
		var node = maze.nodes[node_idx]
		var node_symbol = maze.get_node_symbol_by_idx(node_idx)
		var node_weight = Constants.weight_mapping[node_symbol]
		add_node(str(node_idx), node, node_weight)

func _connect_nodes():
	for node_idx in len(maze.nodes):
		for neighbour_direction in Constants.directions.values():
			var node = maze.nodes[node_idx]
			var neighbour_node = node + neighbour_direction
			if neighbour_node in maze.nodes:
				connect_nodes(str(node_idx), str(maze.get_node_index(neighbour_node)))

func _add_connection(idx: String, to_idx: String):
	if not idx in connections:
		connections[idx] = []
	if not to_idx in connections[idx]:
		connections[idx].append(to_idx)
