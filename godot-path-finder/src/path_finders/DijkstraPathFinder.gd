extends AbstractPathFinder
class_name DijkstraPathFinder

var default_distance = 1e7
var transition_cost = {}
var transition_node = {}

func set_graph(graph_):
	graph = graph_
	for node_name in graph.nodes:
		transition_cost[node_name] = default_distance
	for node_name in graph.nodes:
		transition_node[node_name] = null
	transition_cost[graph.start_node] = 0

func get_node_path():
	"""Finds a path from start_node to end_node using depth first search approach.

	Returns:
		path (list): A list containing node coordinates which form a path from start to end.
	"""
	_calculate_transitions()
	
	var start_node = graph.start_node
	var current_node = graph.end_node
	
	var path = [graph.nodes[current_node]['position']]
	while current_node != start_node:
		current_node = transition_node[current_node]
		path.append(graph.nodes[current_node]['position'])
	path.invert()
	return path

func _calculate_transitions():
	var unvisited_nodes = []
	for node_name in graph.nodes:
		unvisited_nodes.append(node_name)
	
	while len(unvisited_nodes) > 0:
		var current_node = _get_minimum_cost_node(unvisited_nodes)
		if not current_node:
			break
		unvisited_nodes.erase(current_node)
		for node_position in _get_connected_nodes(current_node):
			var connected_node = graph.get_position_index(node_position)
			var connected_node_weight = graph.get_position_weight(node_position)
			var trainsition_weight = transition_cost[current_node] + connected_node_weight
			if transition_cost[connected_node] > trainsition_weight:
				transition_cost[connected_node] = trainsition_weight
				transition_node[connected_node] = current_node

func _get_minimum_cost_node(unvisited_nodes):
	var min_cost_node = null
	var min_distance = default_distance
	for node_name in unvisited_nodes:
		if transition_cost[node_name] < min_distance:
			min_distance = transition_cost[node_name]
			min_cost_node = node_name
	return min_cost_node

func _get_connected_nodes(node_name):
	var connected_nodes = []
	var current_position = graph.nodes[node_name]['position']
	for move_vector in Constants.directions.values():
		var next_position = current_position + move_vector
		if _is_valid_move(current_position, next_position) and \
			not _is_obstacle(next_position):
			connected_nodes.append(next_position)
	return connected_nodes
