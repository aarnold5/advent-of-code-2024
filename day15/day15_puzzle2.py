from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

def solve_day15_puzzle2():
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
                c = line[i]
                if c == '#' or c == '.':
                    map[line_idx].append(c)
                    map[line_idx].append(c)
                elif c == 'O':
                    map[line_idx].append('[')
                    map[line_idx].append(']')
                elif c == '@':
                    curr_coords = (len(map[line_idx]), line_idx)
                    map[line_idx].append('@')
                    map[line_idx].append('.')
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
            if map[y][x] == '[':
                gps_sum += 100 * y + x
    return gps_sum

def try_move_up(curr_coords, map):
    (curr_x, curr_y) = curr_coords
    new_coords = curr_coords
    if map[curr_y-1][curr_x] == '.':
        map[curr_y-1][curr_x] = '@'
        new_coords = (curr_x,curr_y-1)
        map[curr_y][curr_x] = '.'
    else:
        to_check = {curr_y: [curr_x]}
        top_layers = {}
        all_clear = True
        for iy in range(curr_y-1, 0, -1):
            to_check[iy] = []
            for x in to_check[iy+1]:
                if map[iy][x] == '#':
                    return new_coords
                elif map[iy][x] == '[':
                    to_check[iy].append(x)
                    to_check[iy].append(x+1)
                    top_layers[x] = iy
                elif map[iy][x] == ']':
                    to_check[iy].append(x)
                    to_check[iy].append(x-1)
                    top_layers[x] = iy

        for x in top_layers:
            if map[top_layers[x]-1][x] != '.':
                all_clear = False

        if all_clear and len(top_layers) > 0:
            for y in range(min(top_layers.values())-1, curr_y):
                for x in to_check[y+1]:
                    map[y][x] = map[y+1][x]
                for x in to_check[y]:
                    if x not in to_check[y+1]:
                        map[y][x] = '.'
            map[curr_y][curr_x] = '.'
            new_coords = (curr_x,curr_y-1)
        else:
            return new_coords
            
    return new_coords
    

def try_move_down(curr_coords, map):
    (curr_x, curr_y) = curr_coords
    new_coords = curr_coords
    if map[curr_y+1][curr_x] == '.':
        map[curr_y+1][curr_x] = '@'
        new_coords = (curr_x,curr_y+1)
        map[curr_y][curr_x] = '.'
    else:
        to_check = {curr_y: [curr_x]}
        top_layers = {}
        all_clear = True
        for iy in range(curr_y+1, len(map)):
            to_check[iy] = []
            for x in to_check[iy-1]:
                if map[iy][x] == '#':
                    return new_coords
                elif map[iy][x] == '[':
                    to_check[iy].append(x)
                    to_check[iy].append(x+1)
                    top_layers[x] = iy
                elif map[iy][x] == ']':
                    to_check[iy].append(x)
                    to_check[iy].append(x-1)
                    top_layers[x] = iy
            
        for x in top_layers:
            if map[top_layers[x]+1][x] != '.':
                all_clear = False

        if all_clear and len(top_layers) > 0:
            for y in range(max(top_layers.values())+1, curr_y, -1):
                for x in to_check[y-1]:
                    map[y][x] = map[y-1][x]
                for x in to_check[y]:
                    if x not in to_check[y-1]:
                        map[y][x] = '.'
            map[curr_y][curr_x] = '.'
            new_coords = (curr_x,curr_y+1)
        else:
            return new_coords
            
    return new_coords


def try_move_left(curr_coords, map):
    (curr_x, curr_y) = curr_coords
    new_coords = curr_coords

    if map[curr_y][curr_x-1] == ']':
        for ix in range(curr_x-1, 0, -1):
            if map[curr_y][ix] == '#':
                return new_coords
            if map[curr_y][ix] == '.':
                for i in range(ix, curr_x):
                    map[curr_y][i] = map[curr_y][i+1]
                map[curr_y][curr_x] = '.'
                new_coords = (curr_x-1,curr_y)
                break
    elif map[curr_y][curr_x-1] == '.':
        map[curr_y][curr_x-1] = '@'
        new_coords = (curr_x-1,curr_y)
        map[curr_y][curr_x] = '.'
    return new_coords


def try_move_right(curr_coords, map):
    (curr_x, curr_y) = curr_coords
    new_coords = curr_coords

    if map[curr_y][curr_x+1] == '[':
        for ix in range(curr_x+1, len(map[0])):
            if map[curr_y][ix] == '#':
                return new_coords
            if map[curr_y][ix] == '.':
                for i in range(ix, curr_x, -1):
                    map[curr_y][i] = map[curr_y][i-1]
                map[curr_y][curr_x] = '.'
                new_coords = (curr_x+1,curr_y)
                break
    elif map[curr_y][curr_x+1] == '.':
        map[curr_y][curr_x+1] = '@'
        new_coords = (curr_x+1,curr_y)
        map[curr_y][curr_x] = '.'
    return new_coords

    
def try_move(curr_coords, direction, map):
    if direction == Direction.UP:
        new_coords = try_move_up(curr_coords, map)

    elif direction == Direction.DOWN:
        new_coords = try_move_down(curr_coords, map)

    elif direction == Direction.LEFT:
        new_coords = try_move_left(curr_coords, map)

    elif direction == Direction.RIGHT:
        new_coords = try_move_right(curr_coords, map)

    return new_coords


def print_map(map):
    for y in map:
        print(str(y)+'\n')


print(solve_day15_puzzle2())