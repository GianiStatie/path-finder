from src.constants import directions
from src.utils import add_vectors

from .abstract_path_finder import AbstractPathFinder

class BFSPathFinder(AbstractPathFinder):
    """ Subclass of AbstractPathFinder
    Finds the path using breadth first search approach.

    """

    def get_node_path(self):
        """Generates a path from the graph's start_node to the end_node.

        Returns:
            path (list): List of points which lead from start_node to end_node.
        """
        moves = [""]

        while len(moves) != 0:
            current_move = moves.pop(0)
            for direction in directions:
                # we take a step in each cardinal direction and check
                # its validity by calling _walk_path
                next_move = direction if not current_move else current_move + direction
                walk_result = self._walk_path(next_move)

                # if we found the end we end the loop
                if walk_result['is_valid']:
                    moves.append(next_move)

                # if we found a valid path, we add it to the improvised FIFO
                if walk_result['is_end']:
                    return walk_result['path']
        return []

    def _walk_path(self, move_sequence: str):
        meta = {
            'is_end': False,
            'is_valid': False,
            'path': []
        }
        visited_nodes = []
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
            if new_position in visited_nodes:
                return meta
            visited_nodes.append(new_position)
            current_position = new_position

        meta['is_valid'] = True
        meta['is_end'] = current_position == self.graph.get_end_node_position()
        return meta
