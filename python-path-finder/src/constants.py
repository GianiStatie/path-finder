START_CHAR = 'S'
END_CHAR = 'E'
OBSTACLE_CHAR = '#'

directions = {
    'U': [0, -1],
    'D': [0, 1],
    'L': [-1, 0],
    'R': [1, 0]
}

weight_mapping = {
    " ": 1.0,
    "S": 1.0,
    "E": 1.0,
    "H": 10.0,
    "#": 999.0
}
