import argparse

from maze import Maze
from path_finders import get_algorithm

def print_path(maze, path, exclude_bounds=True):
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

    maze = Maze()
    algorithm = get_algorithm(args.algorithm)
    algorithm.initialize_node_graph(maze)
    path = algorithm.get_node_path()

    print_path(maze, path)