from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

def solve_day6_puzzle1():
    f = open("inputs/day-6.txt", "r")

    map = []
    curr_coords = (0,0)
    curr_direction = Direction.UP
    positions = set()
    line_idx = 0

    for line in f:
        map.append(line.strip())
        foundIdx = line.find('^')
        if foundIdx != -1:
            curr_coords = (foundIdx, line_idx)
            positions.add(curr_coords)
        line_idx += 1
            
    f.close()

    while next_step_in_range(map, curr_direction, curr_coords):
        new_pos = get_next_pos(curr_direction, curr_coords)
        if can_move_forward(map, new_pos):
            curr_coords = new_pos
            positions.add(curr_coords)
        else:
            if curr_direction == Direction.UP:
                curr_direction = Direction.RIGHT
            elif curr_direction == Direction.RIGHT:
                curr_direction = Direction.DOWN
            elif curr_direction == Direction.DOWN:
                curr_direction = Direction.LEFT
            elif curr_direction == Direction.LEFT:
                curr_direction = Direction.UP

    return len(positions)


def can_move_forward(map, forward_coords):
    (x,y) = forward_coords
    if map[y][x] != '#':
        return True
    else:
        return False


def get_next_pos(direction, coords):
    new_x = coords[0] + direction.value[0]
    new_y = coords[1] + direction.value[1]
    return (new_x, new_y)


def next_step_in_range(map, direction, coords):
    next_pos = get_next_pos(direction, coords)
    if next_pos[0] >= 0 and next_pos[0] <= len(map[0]) - 1 and next_pos[1] >= 0 and next_pos[1] <= len(map) - 1:
        return True
    else:
        return False


print(solve_day6_puzzle1())