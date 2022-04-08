extends AbstractPathFinder
class_name DijkstraPathFinder

var default_distance = 1e7
var transition_cost = []
var transition_node = []

func set_graph(graph_):
	graph = graph_
	for i in range(len(graph.nodes)):
		transition_cost.append(default_distance)
	for i in range(len(graph.nodes)):
		transition_node.append(null)
	transition_cost[int(graph.start_node)] = 0

func get_node_path():
	"""Finds a path from start_node to end_node using depth first search approach.

	Returns:
		path (list): A list containing node coordinates which form a path from start to end.
	"""
	_calculate_transitions()
	
	var start_node = self.graph.start_node
	var current_node = self.graph.end_node
	
	var path = [graph.nodes[current_node]['position']]
	while current_node != start_node:
		current_node = transition_cost[current_node]
		path.append(graph.nodes[current_node]['position'])
	return path

func _calculate_transitions():
	var unvisited_nodes = graph.nodes.keys()
	
	while len(unvisited_nodes) > 0:
		var current_node = _get_minimum_cost_index(unvisited_nodes)
		if current_node == -1:
			break
		unvisited_nodes.remove(current_node)
		for connected_node in _get_connected_nodes(current_node):
			var connected_node_idx = int(graph.get_position_index(connected_node))
			var connected_node_weight = graph.get_position_weight(connected_node)
			var trainsition_weight = transition_cost[current_node] + connected_node_weight
			if transition_cost[connected_node_idx] > trainsition_weight:
				transition_cost[connected_node_idx] = trainsition_weight
				transition_node[connected_node_idx] = current_node

func _get_minimum_cost_index(unvisited_nodes):
	var min_index = -1
	var min_distance = default_distance
	for idx in unvisited_nodes:
		idx = int(idx)
		if transition_cost[idx] < min_distance:
			min_distance = transition_cost[idx]
			min_index = idx
	return min_index

func _get_connected_nodes(node_idx):
	var connected_nodes = []
	var current_position = graph.nodes[str(node_idx)]['position']
	for move_vector in Constants.directions.values():
		var next_position = current_position + move_vector
		if _is_valid_move(current_position, next_position) and \
			not _is_obstacle(next_position):
			connected_nodes.append(next_position)
	return connected_nodes
