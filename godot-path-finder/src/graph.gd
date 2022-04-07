extends Node
class_name Graph

var start_node
var end_node
var nodes = {}
var connections = {}
var obstacle_weight = Constants.weight_mapping[Constants.OBSTACLE_CHAR]

var maze

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

func get_start_node_position():
	"""Gets the position of the start node.

	Returns:
		position (list): Position of the node relative to the maze.
	"""
	return nodes[start_node]['position']

func get_end_node_position():
	"""Gets the position of the end node.

	Returns:
		position (list): Position of the node relative to the maze.
	"""
	return nodes[end_node]['position']

func get_position_index(position: Vector2):
	"""Gets the index of a node based on its position relative to the maze.

	Args:
		position (list): Position of the node relative to the maze.

	Returns:
		node_idx (int): Index of the node based on its position.
			Returns -1 if the node is not contained in the maze.
	"""
	for node_idx in nodes:
		var node = nodes[node_idx]
		if node['position'] == position:
			return node_idx
	return null

func get_position_weight(position: Vector2):
	"""Gets the weight of a node based on its position relative to the maze.

	Args:
		position (list): Position of the node relative to the maze.

	Returns:
		weight (float): Weight of the node based on its position.
			Returns self.obstacle_weight if the node is not contained in the maze.
	"""
	for node in nodes.values():
		if node['position'] == position:
			return node['weight']
	return obstacle_weight

func get_all_node_positions():
	"""Gets a list containing all node position in order.

	Returns:
		positions (list): List of graph nodes positions.
	"""
	var positions = []
	for node in nodes.values():
		positions.append(node['position'])
	return positions

func _add_nodes():
	for node in maze.nodes:
		var node_idx = maze.get_node_index(node)
		var node_symbol = maze.get_node_symbol_by_idx(node_idx)
		var node_weight = Constants.weight_mapping[node_symbol]
		add_node(str(node_idx), node, node_weight)
	start_node = str(maze.start_node_idx)
	end_node = str(maze.end_node_idx)

func _connect_nodes():
	for node in maze.nodes:
		var node_idx = maze.get_node_index(node)
		for neighbour_direction in Constants.directions.values():
			var neighbour_node = node + neighbour_direction
			if neighbour_node in maze.nodes:
				connect_nodes(str(node_idx), str(maze.get_node_index(neighbour_node)))

func _add_connection(idx: String, to_idx: String):
	if not idx in connections:
		connections[idx] = []
	if not to_idx in connections[idx]:
		connections[idx].append(to_idx)
