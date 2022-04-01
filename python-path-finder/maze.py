from constants import start_char, end_char

maze_template = [
    ["#","#", "#", "#", "#", "S","#"],
    ["#"," ", " ", " ", "#", " ","#"],
    ["#"," ", "#", " ", "#", " ","#"],
    ["#","E", "#", " ", " ", " ","#"],
    ["#"," ", "#", "#", "#", " ","#"],
    ["#"," ", " ", " ", "#", " ","#"],
    ["#","#", "#", "#", "#", "#","#"]
]

class Maze:
    def __init__(self, template:list[list]=None):
        self.nodes = []
        self.start_node = None
        self.end_node = None
        self.maze_template = template or maze_template

        self._init_map()

    def _init_map(self):
        for y in range(len(maze_template)):
            for x in range(len(maze_template[0])):
                maze_cell_symbol = maze_template[y][x]
                if maze_cell_symbol == start_char: self.start_node = self.get_node_index([x, y])
                if maze_cell_symbol == end_char: self.end_node = self.get_node_index([x, y])
                self.nodes.append([x, y])

    def get_node_index(self, node: list):
        maze_height = len(self.maze_template)
        return node[1] * maze_height + node[0]

    def get_node_symbol(self, node: list):
        node_idx = self.get_node_index(node)
        return self.get_node_symbol_by_idx(node_idx)

    def get_node_symbol_by_idx(self, node_idx: int):
        maze_height = len(self.maze_template)
        i, j = node_idx // maze_height, node_idx % maze_height
        return maze_template[i][j]
    
    