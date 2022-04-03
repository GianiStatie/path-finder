from .constants import START_CHAR, END_CHAR

maze_template = [
    ["#","#", "#", "#", "#", "S","#"],
    ["#","E", " ", " ", "#", " ","#"],
    ["#"," ", "#", " ", "#", " ","#"],
    ["#"," ", "#", "H", " ", " ","#"],
    ["#"," ", "#", "#", "#", " ","#"],
    ["#"," ", " ", " ", " ", " ","#"],
    ["#","#", "#", "#", "#", "#","#"]
]

class Maze:
    """Creates maze object which stores maze nodes, weights and symbolic notation.

    """
    def __init__(self, template:list[list]=None):
        self.nodes = []
        self.start_node = None
        self.end_node = None
        self.maze_template = template or maze_template

        self._init_map()

    def _init_map(self):
        for row_idx, row in enumerate(maze_template):
            for col_idx, maze_cell_symbol in enumerate(row):
                if maze_cell_symbol == START_CHAR:
                    self.start_node = self.get_node_index([col_idx, row_idx])
                if maze_cell_symbol == END_CHAR:
                    self.end_node = self.get_node_index([col_idx, row_idx])
                self.nodes.append([col_idx, row_idx])

    def get_node_index(self, node: list):
        """Takes as input the coordinates of a node and returns its index.

        Args:
            node (list): Node coordinates relative to the maze.

        Returns:
            node_idx (int): Index of the node relative to the maze.
        """
        maze_height = len(self.maze_template)
        return node[1] * maze_height + node[0]

    def get_node_symbol(self, node: list):
        """Takes as input the coordinates of a node and returns its symbol.

        Args:
            node (list): Node coordinates relative to the maze.

        Returns:
            node_symbol (str): Symbol denoting the type of node.
        """
        node_idx = self.get_node_index(node)
        return self.get_node_symbol_by_idx(node_idx)

    def get_node_symbol_by_idx(self, node_idx: int):
        """Takes as input the index of a node and returns its symbol.

        Args:
            node_idx (int): Node index relative to the maze.

        Returns:
            node_symbol (str): Symbol denoting the type of node.
        """
        maze_height = len(self.maze_template)
        i, j = node_idx // maze_height, node_idx % maze_height
        return maze_template[i][j]
    