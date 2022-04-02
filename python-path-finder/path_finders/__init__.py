from .bfs_path_finder import BFSPathFinder
from .dfs_path_finder import DFSPathFinder

def get_algorithm(name: str):
    if name.lower() == 'bfs':
        return BFSPathFinder()
    elif name.lower() == 'dfs':
        return DFSPathFinder()
    else:
        raise ValueError(name)