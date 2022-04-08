extends Node

func generate_adjacent_nodes(node: Vector2):
	"""Retruns a generator with neighbours of given node.

	Args:
		node (Vector2): Node for which to fetch the neighbours.

	Yields:
		neighbour (Vector2): One of the neighbours of given node.
	"""
	var adjecent_nodes = []
	for direction in Constants.directions.values():
		adjecent_nodes.append(node + direction)
	return adjecent_nodes

func euclidean_distance(vect_a: Vector2, vect_b: Vector2):
	"""Calculates the euclidean distance between two vectors.

	Args:
		vect_a (Vector2): First vector.
		vect_b (Vector2): Second vector.

	Returns:
		distance (float): The distance between the two vectors.
	"""
	return pow(vect_a.x - vect_b.x, 2) + pow(vect_a.y - vect_b.y, 2)
