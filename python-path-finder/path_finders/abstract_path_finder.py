from maze import Maze
from constants import directions, weight_mapping, OBSTACLE_CHAR
from utils import add_vectors

class AbstractPathFinder:
    """Abstract Class for PathFinder class containing common methods.

    """
    def __init__(self):
        self.nodes = {}
        self.connections = {}
        self.start_node = None
        self.end_node = None
        self.obstacle_weight = weight_mapping[OBSTACLE_CHAR]

    def initialize_node_graph(self, maze: Maze):
        """Extracts information regarding node type and placement from a maze object
        and creates a graph-like structure.

        Args:
            maze (Maze): Object containing node position, weight and type.
        """
        self._add_nodes(maze)
        self._connect_nodes(maze)
        self.start_node = maze.start_node
        self.end_node = maze.end_node

    def add_node(self, id_: int, position: list, weight: float = 1.0):
        """Adds node to the internal graph-like structure which describes the maze.

        Args:
            id_ (int): Index of the node relative to the maze.
            position (list): Coordinates of the node relative to the maze.
            weight (float, optional): Weight of the node denoted by its symbol. Defaults to 1.0.
        """
        self.nodes[id_] = {
            "position": position,
            "weight": weight
        }

    def connect_nodes(self, id_: int, to_id: int, bidirectional: bool = True):
        """Adds a connection between two nodes in the internal graph-like structure.

        Args:
            id_ (int): Index of the parent node.
            to_id (int): Index of the child node.
            bidirectional (bool, optional): Whether the child is also connected to the parent.
                Defaults to True.
        """
        self._add_connection(id_, to_id)
        if bidirectional:
            self._add_connection(id_ = to_id, to_id = id_)

    def get_node_path(self):
        """Generates a path from the start_node to the end_node.

        Raises:
            NotImplementedError: Cannot be called from the abstract class.
        """
        raise NotImplementedError

    def _add_nodes(self, maze: Maze):
        for node_idx, node in enumerate(maze.nodes):
            node_weight = weight_mapping[maze.get_node_symbol_by_idx(node_idx)]
            self.add_node(node_idx, node, node_weight)

    def _connect_nodes(self, maze: Maze):
        for node_idx, node in enumerate(maze.nodes):
            for neighbour_direction in directions.values():
                neighbour_node = add_vectors(node, neighbour_direction)
                if neighbour_node in maze.nodes:
                    self.connect_nodes(node_idx, maze.get_node_index(neighbour_node))

    def _add_connection(self, id_: int, to_id: int):
        if id_ not in self.connections:
            self.connections[id_] = []
        if to_id not in self.connections[id_]:
            self.connections[id_].append(to_id)

    def _get_position_index(self, position: list):
        for node_idx, node in self.nodes.items():
            if node['position'] == position:
                return node_idx
        return -1

    def _get_position_weight(self, position: list):
        for node in self.nodes.values():
            if node['position'] == position:
                return node['weight']
        return self.obstacle_weight

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
        cur_position_idx = self._get_position_index(current_position)
        new_position_idx = self._get_position_index(new_position)
        if cur_position_idx >= 0 and new_position_idx >= 0:
            if new_position_idx in self.connections[cur_position_idx]:
                return True
        return False

    def _is_obstacle(self, position: list):
        return self._get_position_weight(position) == self.obstacle_weight

    def _walk_path(self, move_sequence: str):
        meta = {
            'is_end': False,
            'is_valid': False,
            'path': []
        }
        current_position = self.nodes[self.start_node]['position']
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
        meta['is_end'] = current_position == self.nodes[self.end_node]['position']
        return meta
    