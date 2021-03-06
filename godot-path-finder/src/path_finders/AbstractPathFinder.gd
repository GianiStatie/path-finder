extends Node
class_name AbstractPathFinder

var graph setget set_graph
var obstacle_weight = Constants.weight_mapping[Constants.OBSTACLE_CHAR]

var start_node_position
var end_node_position

func _is_redundand_move(move_sequence: String):
	var move_direction = Vector2.ZERO
	if len(move_sequence) > 1:
		move_direction = Constants.directions[move_sequence[-1]] + \
			Constants.directions[move_sequence[-2]]
		if move_direction == Vector2.ZERO:
			return true
	return false

func _is_valid_move(current_position:Vector2, new_position: Vector2):
	var cur_position_idx = graph.get_position_index(current_position)
	var new_position_idx = graph.get_position_index(new_position)
	if cur_position_idx != null and new_position_idx != null:
		if new_position_idx in self.graph.connections[cur_position_idx]:
			return true
	return false

func _is_obstacle(position: Vector2):
	return graph.get_position_weight(position) == obstacle_weight

func set_graph(value):
	graph = value
	start_node_position = graph.get_start_node_position()
	end_node_position = graph.get_end_node_position()
