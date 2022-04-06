from re import M
from .maze import Maze
from .maze_procedural import MazeProcedural

def get_maze(type):
    if type == 'simple':
        return Maze()
    if type == 'procedural':
        return MazeProcedural(10, 10)