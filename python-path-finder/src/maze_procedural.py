import random

from src.maze import Maze
from src.utils import generate_adjacent_nodes, add_vectors
from src.constants import START_CHAR, END_CHAR, EMPTY_CHAR, OBSTACLE_CHAR

# look over this: https://github.com/OrWestSide/python-scripts/blob/master/maze.py

class MazeProcedural(Maze):
    def __init__(self, width, height):
        maze_template = self.generate_maze(width, height)
        super().__init__(maze_template)

    def generate_maze(self, width, height):
        width += 1 
        height += 1
        rows, cols = height, width

        maze = {}

        spaceCells = set()
        connected = set()
        walls = set()

        # Initialize with grid.
        for i in range(rows):
            for j in range(cols):
                if (i%2 == 1) and (j%2 == 1):
                    maze[(i,j)] = EMPTY_CHAR
                else:
                    maze[(i,j)] = OBSTACLE_CHAR
        
        # Fill in border.
        for i in range(rows):
            maze[(i,0)] = OBSTACLE_CHAR
            maze[(i,cols-1)] = OBSTACLE_CHAR
        for j in range(cols):
            maze[(0,j)] = OBSTACLE_CHAR
            maze[(rows-1,j)] = OBSTACLE_CHAR

        for i in range(rows):
            for j in range(cols):
                if maze[(i,j)] == EMPTY_CHAR:
                    spaceCells.add((i,j))
                if maze[(i,j)] == OBSTACLE_CHAR:
                    walls.add((i,j))

        # Prim's algorithm to knock down walls.
        connected.add((1,1))
        while len(connected) < len(spaceCells):
            doA, doB = None, None
            cns = list(connected)
            random.shuffle(cns)
            for (i,j) in cns:
                if doA is not None: break
                for A, B in generate_adjacent_nodes((i,j)):
                    if A not in walls: 
                        continue
                    if (B not in spaceCells) or (B in connected):
                        continue
                    doA, doB = A, B
                    break
            A, B = doA, doB
            maze[A] = EMPTY_CHAR
            walls.remove(A)
            spaceCells.add(A)
            connected.add(A)
            connected.add(B)

        # Insert character and goals.
        TL = (1,1)
        BR = (rows-2, cols-2)
        if rows % 2 == 0:
            BR = (BR[0]-1, BR[1])
        if cols % 2 == 0:
            BR = (BR[0], BR[1]-1)

        maze[TL] = START_CHAR
        maze[BR] = END_CHAR

        maze_template = []
        txt = []
        for i in range(rows):
            maze_template.append([maze[(i,j)] for j in range(cols)])
            txt.append("".join(maze[(i,j)] for j in range(cols)))
        print('\n'.join(txt))

        return maze_template
        