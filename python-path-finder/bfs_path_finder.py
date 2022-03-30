import queue

maze = [
    ["#","#", "#", "#", "#", "O","#"],
    ["#"," ", " ", " ", "#", " ","#"],
    ["#"," ", "#", " ", "#", " ","#"],
    ["#"," ", "#", " ", " ", " ","#"],
    ["#"," ", "#", "#", "#", " ","#"],
    ["#"," ", "X", " ", "#", " ","#"],
    ["#","#", "#", "#", "#", "#","#"]
]

start_pos = [5, 0]

directions = {
    'U': [0, -1],
    'D': [0, 1],
    'L': [-1, 0],
    'R': [1, 0]
}

def add_vectors(vect_a, vect_b):
    return list(map(sum, zip(vect_a, vect_b)))

def get_node(vect):
    return maze[vect[1]][vect[0]]

def is_outside_bounds(pos):
    if 0 <= pos[0] < len(maze[0]) and 0 < pos[1] <= len(maze):
        return False
    return True

def is_valid(moves):
    if len(moves) >= 2:
        last_moves_sum = add_vectors(directions[moves[-1]], directions[moves[-2]])
        if last_moves_sum == [0, 0]:
            return False

    current_pos = start_pos
    for direction in moves:
        move_direction = directions[direction]
        current_pos = add_vectors(current_pos, move_direction)
        if is_outside_bounds(current_pos):
            return False
        elif get_node(current_pos) == '#':
            return False
    return True

def is_end_path(moves):
    current_pos = start_pos
    for direction in moves:
        move_direction = directions[direction]
        current_pos = add_vectors(current_pos, move_direction)
    if get_node(current_pos) == 'X':
        return True
    return False

if __name__ == '__main__':
    moves = queue.Queue()
    moves.put("")

    last_move = ""
    end_path = ""

    while not end_path:
        last_move = moves.get()
        for direction in directions.keys():
            current_move = last_move + direction
            if is_valid(current_move):
                moves.put(current_move)
                if is_end_path(current_move):
                    end_path = current_move
                    break

    print(end_path)
