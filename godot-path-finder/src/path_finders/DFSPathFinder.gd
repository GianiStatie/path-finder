extends AbstractPathFinder
class_name DFSPathFinder

func get_node_path():
	"""Finds a path from start_node to end_node using depth first search approach.

	Returns:
		path (list): A list containing node coordinates which form a path from start to end.
	"""
	var moves = [""]
	return _dfs(moves)

func _dfs(moves):
	if len(moves) == 0:
		return []
	
	var current_move: String = moves.pop_back()
	for direction in Constants.directions:
		# we take a step in each cardinal direction and check
		# its validity by calling _walk_path
		var next_move = current_move + direction
		var walk_result = _walk_path(next_move)
		
		# if we found the end we end the loop
		if walk_result['is_end']:
			return walk_result['path']
		
		# if we found a valid path, we continue down on it
		if walk_result['is_valid']:
			moves.append(next_move)
			
			# the path is bigger than 0 when it's the end
			var path = _dfs(moves)
			if len(path) > 0:
				return path
	return []

func _walk_path(move_sequence: String):
	var meta = {
		'is_end': false,
		'is_valid': false,
		'path': []
	}
	var visited_nodes = []
	var current_position = graph.get_start_node_position()
	meta['path'].append(current_position)
	
	if _is_redundand_move(move_sequence):
		return meta
	
	for direction in move_sequence:
		var new_position = current_position + Constants.directions[direction]
		meta['path'].append(new_position)
		if not _is_valid_move(current_position, new_position):
			return meta
		if _is_obstacle(new_position):
			return meta
		if new_position in visited_nodes:
			return meta
		visited_nodes.append(new_position)
		current_position = new_position
	
	meta['is_valid'] = true
	meta['is_end'] = current_position == graph.get_end_node_position()
	return meta
