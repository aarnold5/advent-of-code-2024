from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

def solve_day15_puzzle1():
    f = open('inputs/day-15.txt', 'r')

    map = []
    curr_coords = (0,0)
    line_idx = 0
    directions = []

    second_half = False

    for line in f:
        if line == '\n':
            second_half = True
        elif not second_half:
            map.append([])
            line = line.strip()
            for i in range(len(line)):
                map[line_idx].append(line[i])
                if line[i] == '@':
                    curr_coords = (i, line_idx)
            line_idx += 1
        else:
            for c in line:
                if c == '<':
                    directions.append(Direction.LEFT)
                elif c == '>':
                    directions.append(Direction.RIGHT)
                elif c == '^':
                    directions.append(Direction.UP)
                elif c == 'v':
                    directions.append(Direction.DOWN)
    f.close()
    
    for direction in directions:
        curr_coords = try_move(curr_coords, direction, map)

    return sum_gps(map)


def sum_gps(map):
    gps_sum = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 'O':
                gps_sum += 100 * y + x
    return gps_sum

    
def try_move(curr_coords, direction, map):
    (curr_x, curr_y) = curr_coords
    new_coords = curr_coords

    if direction == Direction.UP:
        if map[curr_y-1][curr_x] == 'O':
            for iy in range(curr_y-1, -1, -1):
                if map[iy][curr_x] == '#':
                    return new_coords
                if map[iy][curr_x] == '.':
                    if map[curr_y-1][curr_x] == 'O':
                        map[iy][curr_x] = 'O'
                    map[curr_y-1][curr_x] = '@'
                    new_coords = (curr_x,curr_y-1)
                    map[curr_y][curr_x] = '.'
                    break
        elif map[curr_y-1][curr_x] == '.':
            map[curr_y-1][curr_x] = '@'
            new_coords = (curr_x,curr_y-1)
            map[curr_y][curr_x] = '.'

    elif direction == Direction.DOWN:
        if map[curr_y+1][curr_x] == 'O':
            for iy in range(curr_y+1, len(map)):
                if map[iy][curr_x] == '#':
                    return new_coords
                if map[iy][curr_x] == '.':
                    if map[curr_y+1][curr_x] == 'O':
                        map[iy][curr_x] = 'O'
                    map[curr_y+1][curr_x] = '@'
                    new_coords = (curr_x,curr_y+1)
                    map[curr_y][curr_x] = '.'
                    break
        elif map[curr_y+1][curr_x] == '.':
            map[curr_y+1][curr_x] = '@'
            new_coords = (curr_x,curr_y+1)
            map[curr_y][curr_x] = '.'

    elif direction == Direction.LEFT:
        if map[curr_y][curr_x-1] == 'O':
            for ix in range(curr_x-1, -1, -1):
                if map[curr_y][ix] == '#':
                    return new_coords
                if map[curr_y][ix] == '.':
                    if map[curr_y][curr_x-1] == 'O':
                        map[curr_y][ix] = 'O'
                    map[curr_y][curr_x-1] = '@'
                    new_coords = (curr_x-1,curr_y)
                    map[curr_y][curr_x] = '.'
                    break
        elif map[curr_y][curr_x-1] == '.':
            map[curr_y][curr_x-1] = '@'
            new_coords = (curr_x-1,curr_y)
            map[curr_y][curr_x] = '.'

    elif direction == Direction.RIGHT:
        if map[curr_y][curr_x+1] == 'O':
            for ix in range(curr_x+1, len(map[0])):
                if map[curr_y][ix] == '#':
                    return new_coords
                if map[curr_y][ix] == '.':
                    if map[curr_y][curr_x+1] == 'O':
                        map[curr_y][ix] = 'O'
                    map[curr_y][curr_x+1] = '@'
                    new_coords = (curr_x+1,curr_y)
                    map[curr_y][curr_x] = '.'
                    break
        elif map[curr_y][curr_x+1] == '.':
            map[curr_y][curr_x+1] = '@'
            new_coords = (curr_x+1,curr_y)
            map[curr_y][curr_x] = '.'

    return new_coords


def print_map(map):
    for y in map:
        print(str(y)+'\n')


print(solve_day15_puzzle1())