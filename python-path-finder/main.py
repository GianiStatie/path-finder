from maze import Maze
from path_finders.bfs_path_finder import BFSPathFinder
from path_finders.dfs_path_finder import DFSPathFinder

from constants import weight_mapping, directions
from utils import add_vectors

def _add_points(maze, algorithm):
    for node_idx, node in enumerate(maze.nodes):
        node_weight = weight_mapping[maze.get_node_symbol_by_idx(node_idx)]
        algorithm.add_point(node_idx, node, node_weight)

def _connect_points(maze, algorithm):
    for node_idx, node in enumerate(maze.nodes):
        for neighbour_direction in directions.values():
            neighbour_node = add_vectors(node, neighbour_direction)
            if neighbour_node in maze.nodes:
                algorithm.connect_points(node_idx, maze.get_node_index(neighbour_node))

def _get_path(algorithm, start_node, end_node, exclude_bounds=True):
    path = algorithm.get_point_path(start_node, end_node)
    # optional: remove start and end blocks
    if exclude_bounds:
        return path[1:-1]
    return path

def print_path(maze, path):
    maze_template = maze.maze_template
    for node_x, node_y in path:
        maze_template[node_y][node_x] = 'x'
    maze_template = ['  '.join(row) for row in maze_template]
    maze_template = '\n'.join(maze_template)
    print(maze_template)

if __name__ == "__main__":
    maze = Maze()
    algorithm = DFSPathFinder()

    _add_points(maze, algorithm)
    _connect_points(maze, algorithm)
    path = _get_path(algorithm, maze.start_node, maze.end_node)

    print_path(maze, path)