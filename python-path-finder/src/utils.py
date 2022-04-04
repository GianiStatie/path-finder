def add_vectors(vect_a: list, vect_b: list):
    """Does element-wise addition between two lists.

    Args:
        vect_a (list): First vector.
        vect_b (list): Second vector.

    Returns:
        result (list): The result of the vector addition.
    """
    return list(map(sum, zip(vect_a, vect_b)))

def euclidean_distance(vect_a: list, vect_b: list):
    """Calculates the euclidean distance between two vectors.

    Args:
        vect_a (list): First vector.
        vect_b (list): Second vector.

    Returns:
        distance (float): The distance between the two vectors.
    """
    return sum([(i-j)**2 for i, j in zip(vect_a, vect_b)])
