from .bfs_path_finder import BFSPathFinder
from .dfs_path_finder import DFSPathFinder

def get_algorithm(name: str):
    """Fetches a search algorithm object by name.

    Args:
        name (str): Name of the search algorithm.
        Options:
            bfs - Breadth first search algorithm.
            dfs - Deapth first search algorithm.

    Raises:
        ValueError: If the name of the algorithm is not supported.

    Returns:
        Object: Instance of the search algorithm based on given name.
    """
    if name.lower() == 'bfs':
        return BFSPathFinder()
    if name.lower() == 'dfs':
        return DFSPathFinder()
    raise ValueError(name)