START_CHAR = 'S'
END_CHAR = 'E'
EMPTY_CHAR = ' '
OBSTACLE_CHAR = '#'

directions = {
    'U': [0, -1],
    'D': [0, 1],
    'L': [-1, 0],
    'R': [1, 0]
}

weight_mapping = {
    " ": 1.0,  # walkable path
    "S": 1.0,  # start node
    "E": 1.0,  # end node
    "H": 10.0, # hole (shallow obstacle)
    "#": 999.0 # wall (hard obstacle)
}
