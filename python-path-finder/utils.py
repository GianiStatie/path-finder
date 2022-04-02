def add_vectors(vect_a: list, vect_b: list):
    """Does element-wise addition between two lists.

    Args:
        vect_a (list): First vector.
        vect_b (list): Second vector.

    Returns:
        result (list): The result of the vector addition.
    """
    return list(map(sum, zip(vect_a, vect_b)))
