from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)


def solve_day6_puzzle2():
    f = open("inputs/day-6.txt", "r")

    map = []
    start_coords = (0,0)
    line_idx = 0

    # build the map and find the starting position
    for line in f:
        map.append(line.strip())
        foundIdx = line.find('^')
        if foundIdx != -1:
            start_coords = (foundIdx, line_idx)
        line_idx += 1

    f.close()

    # find the positions that get visited
    visited_positions = get_vistited_positions(map, start_coords)

    potential_obstacle_count = 0
    # for each of the positions, try see if adding an obstacle creates a cycle
    for potential_obstacle_pos in visited_positions:
        print("testing " + str(potential_obstacle_pos) + '...')
        result = get_vistited_positions(map, start_coords, potential_obstacle_pos)
        if result == None:
            potential_obstacle_count += 1

    return potential_obstacle_count


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
    

def get_vistited_positions(map, start_coords, obstacle_coord=(-1, -1)):
    positions = set()
    positions.add(start_coords)
    curr_coords = start_coords
    curr_direction = Direction.UP

    directions_changed_to_at_obstacles = {}

    while next_step_in_range(map, curr_direction, curr_coords):
        new_pos = get_next_pos(curr_direction, curr_coords)
        if can_move_forward(map, new_pos) and new_pos != obstacle_coord :
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

            if new_pos in directions_changed_to_at_obstacles:
                # this indicates there is a cycle, so return to break out of the loop
                if curr_direction in directions_changed_to_at_obstacles[new_pos]:
                    return
            else:
                directions_changed_to_at_obstacles[new_pos] = []

            directions_changed_to_at_obstacles[new_pos].append(curr_direction)
    
    return positions


print(solve_day6_puzzle2())