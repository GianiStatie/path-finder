import random

from src.maze import Maze
from src.utils import generate_adjacent_nodes, add_vectors
from src.constants import START_CHAR, END_CHAR, EMPTY_CHAR, OBSTACLE_CHAR

class MazeProcedural(Maze):
    """Procedurally creates maze object which stores maze nodes, weights and symbolic notation.

    """
    def __init__(self, width: int, height: int):
        maze_template = self._generate_maze(width, height)
        super().__init__(maze_template)

    # code yoinked from: https://gist.github.com/gmalmquist/2782000bd6b378831858?fbclid=IwAR0yN1JApyaOeNgtqBxMbj38mxmImzMuVV_xZmt64IZIOuiiPZ237edMjqg
    def _generate_maze(self, width, height):
        width += 2 if width % 2 else 1
        height += 2 if height % 2 else 1
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
        for i in range(rows):
            maze_template.append([maze[(i,j)] for j in range(cols)])

        return maze_template
        