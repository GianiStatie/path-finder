from src.constants import directions, weight_mapping, OBSTACLE_CHAR
from src.maze import Maze
from src.utils import add_vectors

class Graph:
    """Graph-like structure which stores node information and connections.

    """
    def __init__(self):
        self.nodes = {}
        self.connections = {}
        self.start_node = None
        self.end_node = None
        self.obstacle_weight = weight_mapping[OBSTACLE_CHAR]

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
        """Gets the index of a node based on its position relative to the maze.

        Args:
            position (list): Position of the node relative to the maze.

        Returns:
            node_idx (int): Index of the node based on its position.
                Returns -1 if the node is not contained in the maze.
        """
        for node_idx, node in self.nodes.items():
            if node['position'] == position:
                return node_idx
        return -1

    def get_all_node_positions(self):
        """Gets a list containing all node position in order.

        Returns:
            positions (list): List of graph nodes positions.
        """
        return [node['position'] for node in self.nodes.values()]

    def get_position_weight(self, position: list):
        """Gets the weight of a node based on its position relative to the maze.

        Args:
            position (list): Position of the node relative to the maze.

        Returns:
            weight (float): Weight of the node based on its position.
                Returns self.obstacle_weight if the node is not contained in the maze.
        """
        for node in self.nodes.values():
            if node['position'] == position:
                return node['weight']
        return self.obstacle_weight

    def get_start_node_position(self):
        """Gets the position of the start node.

        Returns:
            position (list): Position of the node relative to the maze.
        """
        return self.nodes[self.start_node]['position']

    def get_end_node_position(self):
        """Gets the position of the end node.

        Returns:
            position (list): Position of the node relative to the maze.
        """
        return self.nodes[self.end_node]['position']

    def add_node(self, idx: int, position: list, weight: float = 1.0):
        """Adds node to the internal graph-like structure which describes the maze.

        Args:
            idx (int): Index of the node relative to the maze.
            position (list): Coordinates of the node relative to the maze.
            weight (float, optional): Weight of the node denoted by its symbol. Defaults to 1.0.
        """
        self.nodes[idx] = {
            "position": position,
            "weight": weight
        }

    def connect_nodes(self, idx: int, to_idx: int, bidirectional: bool = True):
        """Adds a connection between two nodes in the internal graph-like structure.

        Args:
            idx (int): Index of the parent node.
            to_idx (int): Index of the child node.
            bidirectional (bool, optional): Whether the child is also connected to the parent.
                Defaults to True.
        """
        self._add_connection(idx, to_idx)
        if bidirectional:
            self._add_connection(idx = to_idx, to_idx = idx)

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

    def _add_connection(self, idx: int, to_idx: int):
        if idx not in self.connections:
            self.connections[idx] = []
        if to_idx not in self.connections[idx]:
            self.connections[idx].append(to_idx)
