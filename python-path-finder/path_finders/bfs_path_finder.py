import sys
sys.path.append("..")

from constants import directions
from .abstract_path_finder import AbstractPathFinder

class BFSPathFinder(AbstractPathFinder):
    def __init__(self):
        super().__init__()

    def get_node_path(self):
        moves = [""]

        while len(moves) != 0:
            current_move = moves.pop(0)
            for direction in directions.keys():
                next_move = direction if not current_move else current_move + direction
                walk_result = self._walk_path(next_move)
                if walk_result['is_valid']: moves.append(next_move)
                if walk_result['is_end']: return walk_result['path']
        return []