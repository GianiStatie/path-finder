from src.constants import directions, weight_mapping
from src.maze import Maze
from src.utils import add_vectors

class Graph:
    def __init__(self):
        self.nodes = {}
        self.connections = {}
        self.start_node = None
        self.end_node = None

    @classmethod
    def from_maze(cls, maze: Maze):
        """Extracts information regarding node type and placement from a maze object
        and creates a graph-like structure.

        Args:
            maze (Maze): Object containing node position, weight and type.
        """
        graph = cls()
        graph._add_nodes(maze)
        graph._connect_nodes(maze)
        graph.start_node = maze.start_node
        graph.end_node = maze.end_node
        return graph

    def get_position_index(self, position: list):
        for node_idx, node in self.nodes.items():
            if node['position'] == position:
                return node_idx
        return -1

    def get_position_weight(self, position: list):
        for node in self.nodes.values():
            if node['position'] == position:
                return node['weight']
        return self.obstacle_weight

    def get_start_node_position(self):
        return self.nodes[self.start_node]['position']

    def get_end_node_position(self):
        return self.nodes[self.end_node]['position']

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