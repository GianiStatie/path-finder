from src.constants import START_CHAR, END_CHAR

MAZE_TEMPLATE = [
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
        self.maze_template = template or MAZE_TEMPLATE

        self._init_map()

    def _init_map(self):
        for row_idx, row in enumerate(self.maze_template):
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
        maze_width = len(self.maze_template[0])
        return node[1] * maze_width + node[0]

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
        maze_width = len(self.maze_template[0])
        i, j = node_idx // maze_width, node_idx % maze_width
        return self.maze_template[i][j]

    def to_text(self, maze_template:list[list]=None):
        """Converts maze template into a string for displaying.

        Args:
            maze_template (list[list], optional): List of nodes to be displayed.
                If not given, self.maze_template will be used.

        Returns:
            maze_template_str (str):
        """
        maze_template_str = []
        maze_template = maze_template or self.maze_template
        for i in range(len(maze_template)):
            maze_template_str.append(
                "".join(maze_template[i][j] for j in range(len(maze_template[0]))))
        return '\n'.join(maze_template_str)

    def print_path(self, path: list, exclude_bounds=True):
        """This function is responsible for displaying the solved maze in the console.
        Args:
            maze (Maze): Maze object containing the ASCII representation of the maze.
            path (list): List of node coordinates which form a path from start to end.
            exclude_bounds (bool, optional): Whether to exclude the start and end nodes in the path. 
                Defaults to True.
        """
        if exclude_bounds:
            path = path[1:-1]

        solved_maze = self.maze_template
        for node_x, node_y in path:
            solved_maze[node_y][node_x] = 'x'
        solved_maze_str = self.to_text(solved_maze)
        print(solved_maze_str)
