import sys
sys.path.append("..")

from constants import directions
from .abstract_path_finder import AbstractPathFinder

class DFSPathFinder(AbstractPathFinder):
    """ Subclass of AbstractPathFinder
    Finds the path using depth first search apporach.

    """
    def _dfs(self, moves):
        if len(moves) == 0:
            return []

        current_move = moves.pop()
        for direction in directions:
            # we take a step in each cardinal direction and check
            # it's validity by calling _walk_path
            next_move = current_move + direction
            walk_result = self._walk_path(next_move)

            # if we found the end we end the loop
            if walk_result['is_end']:
                return walk_result['path']

            # if we found a valid path, we continue down on it
            if walk_result['is_valid']:
                moves.append(next_move)

                # the path is bigger than 0 when it's the end
                path = self._dfs(moves)
                if len(path) > 0:
                    return path
        return []

    def get_node_path(self):
        """Finds a path from start_node to end_node using depth first search approach.

        Returns:
            path (list): A list containing node coordinates which form a path from start to end.
        """
        moves = [""]
        return self._dfs(moves)
