from src.constants import directions, weight_mapping, OBSTACLE_CHAR
from src.utils import add_vectors

class AbstractPathFinder:
    """Abstract Class for PathFinder class containing common methods.

    """
    def __init__(self):
        self.graph = None
        self.obstacle_weight = weight_mapping[OBSTACLE_CHAR]

    def set_graph(self, graph):
        self.graph = graph

    def get_graph(self):
        return self.graph

    def get_node_path(self):
        """Generates a path from the graph's start_node to the end_node.

        Raises:
            NotImplementedError: Cannot be called from the abstract class.
        """
        raise NotImplementedError

    @staticmethod
    def _is_redundand_move(move_sequence: str):
        if len(move_sequence) > 1:
            move_direction = add_vectors(
                directions[move_sequence[-1]],
                directions[move_sequence[-2]])
            if move_direction == [0, 0]:
                return True
        return False

    def _is_valid_move(self, current_position:list, new_position: list):
        cur_position_idx = self.graph.get_position_index(current_position)
        new_position_idx = self.graph.get_position_index(new_position)
        if cur_position_idx >= 0 and new_position_idx >= 0:
            if new_position_idx in self.graph.connections[cur_position_idx]:
                return True
        return False

    def _is_obstacle(self, position: list):
        return self.graph.get_position_weight(position) == self.obstacle_weight

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
    