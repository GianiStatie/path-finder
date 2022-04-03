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
    " ": 1,
    "S": 1,
    "E": 1,
    "#": 999
}
