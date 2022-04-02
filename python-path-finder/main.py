import argparse

from maze import Maze
from path_finders import get_algorithm

def print_path(maze: Maze, path: list, exclude_bounds=True):
    """This function is responsible for displaying the solved maze in the console.
    Args:
        maze (Maze): Maze object containing the ASCII representation of the maze.
        path (list): List of node coordinates which form a path from start to end.
        exclude_bounds (bool, optional): Whether to exclude the start and end nodes in the path. 
            Defaults to True.
    """
    if exclude_bounds:
        path = path[1:-1]

    maze_template = maze.maze_template
    for node_x, node_y in path:
        maze_template[node_y][node_x] = 'x'
    maze_template = ['  '.join(row) for row in maze_template]
    maze_template = '\n'.join(maze_template)
    print(maze_template)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--algorithm', default='dfs',
        help='name of the pathfinding algorithm (dfs, bfs)')
    args = parser.parse_args()

    _maze = Maze()
    _algorithm = get_algorithm(args.algorithm)
    _algorithm.initialize_node_graph(_maze)
    _path = _algorithm.get_node_path()

    print_path(_maze, _path)
