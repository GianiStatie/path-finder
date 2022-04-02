import sys
sys.path.append("..")

from constants import directions
from .abstract_path_finder import AbstractPathFinder

class BFSPathFinder(AbstractPathFinder):
    """ Subclass of AbstractPathFinder
    Finds the path using breadth first search apporach.

    """

    def get_node_path(self):
        moves = [""]

        while len(moves) != 0:
            current_move = moves.pop(0)
            for direction in directions:
                # we take a step in each cardinal direction and check
                # it's validity by calling _walk_path
                next_move = direction if not current_move else current_move + direction
                walk_result = self._walk_path(next_move)

                # if we found the end we end the loop
                if walk_result['is_valid']:
                    moves.append(next_move)

                # if we found a valid path, we add it to the improvised FIFO
                if walk_result['is_end']:
                    return walk_result['path']
        return []
