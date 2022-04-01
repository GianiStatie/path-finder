extends Node
class_name BFS_Pathfinder

var points = {}
var connections = {}
var start_id: int
var end_id: int
var obstacle_weight = 999

var min_x = 0
var min_y = 0
var max_x = 0
var max_y = 0

const directions = {
	'U': Vector2.UP, 
	'D': Vector2.DOWN, 
	'L': Vector2.LEFT, 
	'R': Vector2.RIGHT
	}

func add_point(id: int, position: Vector2, weight_scale: float = 1.0) -> void:
	points[id] = {
		'position': position,
		'weight_scale': weight_scale
	}
	min_x = min(min_x, position.x)
	min_y = min(min_y, position.y)
	max_x = min(max_x, position.x)
	max_y = min(max_y, position.y)

func connect_points(id: int, to_id: int, bidirectional: bool=true) -> void:
	_add_connection(id, to_id)
	if bidirectional: _add_connection(to_id, id)

func get_point_path(from_id: int, to_id: int) -> PoolVector2Array:
	start_id = from_id
	end_id = to_id
	
	var moves = [""]
	var path = []
	var found_end = false
	
	while len(path) == 0 and len(moves) != 0:
		var current_move = moves.pop_front()
		for direction in directions.keys():
			var next_move = direction if not current_move else current_move + direction
			var result = walk_path(next_move)
			if result['is_valid']: moves.append(next_move)
			if result['is_end']:
				path = result['path']
				break
	return path

func walk_path(move_sequence) -> Dictionary:
	var meta = {
		'is_end': false,
		'is_valid': false,
		'path': []
	}
	
	if len(move_sequence) >= 2:
		var last_move_sum = directions[move_sequence[-1]] + directions[move_sequence[-2]]
		if last_move_sum == Vector2.ZERO:
			return meta
	
	var current_pos = points[start_id].position
	for direction in move_sequence:
		current_pos += directions[direction]
		meta['path'].append(current_pos)
		if _is_obstacle(current_pos):
			return meta
	
	meta['is_valid'] = true
	meta['is_end'] = current_pos == points[end_id].position
	return meta

func _add_connection(id:int, to_id:int) -> void:
	if not connections.has(id):
		connections[id] = []
	connections[id].append(to_id)

func _get_position_weight(find_position: Vector2) -> int:
	for pair in points.values():
		var position = pair['position']
		var weight_scale = pair['weight_scale']
		if find_position == position:
			return weight_scale
	return obstacle_weight

func _is_outside_bounds(position: Vector2) -> bool:
	return not ((min_x <= position.x and position.x <= max_x) and \
	 			(min_y <= position.y and position.y <= max_y))

func _is_obstacle(position: Vector2) -> bool:
	return _get_position_weight(position) == obstacle_weight
