import argparse

from src.mazes import get_maze
from src.graph import Graph
from src.path_finders import get_algorithm

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--algorithm', default='astar',
        help='name of the pathfinding algorithm (dfs, bfs, dijkstra, astar)')
    args = parser.parse_args()

    _maze = get_maze('procedural')
    _graph = Graph.from_maze(_maze)

    _algorithm = get_algorithm(args.algorithm)
    _algorithm.set_graph(_graph)
    _path = _algorithm.get_node_path()

    _maze.print_path(_path)
