from src.constants import directions
from src.utils import add_vectors

from .abstract_path_finder import AbstractPathFinder

class DFSPathFinder(AbstractPathFinder):
    """ Subclass of AbstractPathFinder
    Finds the path using depth first search approach.

    """
    def get_node_path(self):
        """Finds a path from start_node to end_node using depth first search approach.

        Returns:
            path (list): A list containing node coordinates which form a path from start to end.
        """
        moves = [""]
        return self._dfs(moves)

    def _dfs(self, moves):
        if len(moves) == 0:
            return []

        current_move = moves.pop()
        for direction in directions:
            # we take a step in each cardinal direction and check
            # its validity by calling _walk_path
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

    def _walk_path(self, move_sequence: str):
        meta = {
            'is_end': False,
            'is_valid': False,
            'path': []
        }
        current_position = self.graph.get_start_node_position()
        meta['path'].append(current_position)

        if self._is_redundand_move(move_sequence):
            return meta

        for direction in move_sequence:
            new_position = add_vectors(current_position, directions[direction])
            meta['path'].append(new_position)
            if not self._is_valid_move(current_position, new_position):
                return meta
            if self._is_obstacle(new_position):
                return meta
            current_position = new_position

        meta['is_valid'] = True
        meta['is_end'] = current_position == self.graph.get_end_node_position()
        return meta
