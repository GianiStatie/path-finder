from maze import Maze
from constants import directions, obstacle_char, weight_mapping
from utils import add_vectors

class AbstractPathFinder:
    def __init__(self):
        self.nodes = {}
        self.connections = {}
        self.start_id = None
        self.end_id = None
        self.obstacle_weight = weight_mapping[obstacle_char]

    def initialize_node_graph(self, maze: Maze):
        self._add_nodes(maze)
        self._connect_nodes(maze)
        self.start_id = maze.start_node
        self.end_id = maze.end_node

    def add_node(self, id: int, position: list, weight: float = 1.0):
        self.nodes[id] = {
            "position": position,
            "weight": weight
        }

    def connect_nodes(self, id: int, to_id: int, bidirectional: bool = True):
        self._add_connection(id, to_id)
        if bidirectional: self._add_connection(to_id, id)

    def get_node_path(self):
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

    def _add_connection(self, id: int, to_id: int):
        # TODO: use this
        if id not in self.connections:
            self.connections[id] = []
        self.connections[id].append(to_id)

    def _get_position_weight(self, position: list):
        for node in self.nodes.values():
            if node['position'] == position:
                return node['weight']
        return self.obstacle_weight

    def _is_redundand_move(self, move_sequence: str):
        if len(move_sequence) > 1:
            move_direction = add_vectors(
                directions[move_sequence[-1]], 
                directions[move_sequence[-2]])
            if move_direction == [0, 0]:
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
        current_position = self.nodes[self.start_id]['position']
        meta['path'].append(current_position)

        if self._is_redundand_move(move_sequence):
            return meta

        for direction in move_sequence:
            current_position = add_vectors(current_position, directions[direction])
            meta['path'].append(current_position)
            if self._is_obstacle(current_position):
                return meta
        
        meta['is_valid'] = True
        meta['is_end'] = current_position == self.nodes[self.end_id]['position']
        return meta

    