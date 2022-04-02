import sys
sys.path.append("..")

from constants import directions
from .abstract_path_finder import AbstractPathFinder

class DFSPathFinder(AbstractPathFinder):
    def __init__(self):
        super().__init__()

    def _dfs(self, moves):
        if len(moves) == 0:
            return []
        
        current_move = moves.pop()
        for direction in directions.keys():
            next_move = direction if not current_move else current_move + direction
            walk_result = self._walk_path(next_move)
            if walk_result['is_end']: return walk_result['path']
            if walk_result['is_valid']:
                moves.append(next_move)
                path = self._dfs(moves)
                if len(path) > 0: return path
        return []

    def get_node_path(self):
        moves = [""]
        return self._dfs(moves)