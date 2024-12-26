from enum import Enum
import heapq
import re


def print_map(map):
    for y in map:
        print(str(y)+'\n')


def check_in_bounds(x, y, map):
    if (x >= 0 and x <= len(map[0])-1 and y >= 0 and y <= len(map)-1) and map[y][x] != '#':
        return True
    else:
        return False
    

def get_neighbors(x, y, map):
    neighbors =[]
    if check_in_bounds(x, y-1, map):
        neighbors.append((x, y-1))
    if check_in_bounds(x-1, y, map):
        neighbors.append((x-1, y))
    if check_in_bounds(x+1, y, map):
        neighbors.append((x+1, y))
    if check_in_bounds(x, y+1, map):
        neighbors.append((x, y+1))
    return neighbors


def get_manhattan_dist(curr, goal):
    return abs(curr[0] - goal[0]) + abs(curr[1] - goal[1])


def get_direction(v_prev, v):
    (v_prev_x, v_prev_y) = v_prev
    (v_x, v_y) = v

    if v_prev_y - 1 == v_y:
        return '^'
    elif v_prev_y + 1 == v_y:
        return 'v'
    elif v_prev_x + 1 == v_x:
        return '>'
    elif v_prev_x - 1 == v_x:
        return '<'
    return 


def get_direction2(dir):
    print(dir)
    if dir == Direction.UP:
        return '^'
    elif dir == Direction.DOWN:
        return 'v'
    elif dir == Direction.RIGHT:
        return '>'
    elif dir == Direction.LEFT:
        return '<'
    return 


class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    

def get_best_path_minimal_turns(start, end, maze):
    queue = []
    seen = set()
    directions = [Direction.RIGHT, Direction.UP, Direction.LEFT, Direction.DOWN]
    back_track = {start: None}

    heapq.heappush(queue, (0, start[0], start[1], 0))
    heapq.heappush(queue, (0, start[0], start[1], 1))
    heapq.heappush(queue, (0, start[0], start[1], 2))
    heapq.heappush(queue, (0, start[0], start[1], 3))
    while len(queue) > 0:
        (curr_dist, curr_x, curr_y, curr_dir_idx) = heapq.heappop(queue)
        if (curr_x, curr_y) == end:
            break
        if (curr_x, curr_y, curr_dir_idx) not in seen and maze[curr_y][curr_x] != '#':
            seen.add((curr_x, curr_y, curr_dir_idx))

            # Try to go in the same direction it's already in
            (curr_dir_x, curr_dir_y) = directions[curr_dir_idx].value
            (new_x, new_y) = (curr_x + curr_dir_x, curr_y + curr_dir_y)
            if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != '#':
                heapq.heappush(queue, (1+curr_dist, new_x, new_y, curr_dir_idx))
                back_track[(new_x, new_y)] = (curr_x, curr_y)

            # Add the neighbors you'd need a clockwise and counterclockwise turn for
            clockwise = curr_dir_idx-1 if curr_dir_idx-1 >= 0 else len(directions)-1
            counterclock = curr_dir_idx+1 if curr_dir_idx+1 < len(directions) else 0

            (cx_dir, cy_dir) = directions[clockwise].value
            (new_x_c, new_y_c) = (curr_x + cx_dir, curr_y + cy_dir)
            if 0 <= new_x_c < len(maze[0]) and 0 <= new_y_c < len(maze) and maze[new_y_c][new_x_c] != '#':
                heapq.heappush(queue, (1000+curr_dist, curr_x, curr_y, clockwise))
            (ccx_dir, ccy_dir) = directions[counterclock].value
            (new_x_cc, new_y_cc) = (curr_x + ccx_dir, curr_y + ccy_dir)
            if 0 <= new_x_cc < len(maze[0]) and 0 <= new_y_cc < len(maze) and maze[new_y_cc][new_x_cc] != '#':
                heapq.heappush(queue, (1000+curr_dist, curr_x, curr_y, counterclock))

    curr = end
    path = ''
    if (end == (0,1) and start == (2,0)):
        print(curr)
    while back_track[curr] != None:
        if (end == (0,1) and start == (2,0)):
            print(back_track[curr])
        (prev_x, prev_y) = back_track[curr]
        (x, y) = curr

        if (prev_x < x): # Right
            for i in range(x-prev_x):
                path = '>' + path
        else:
            for i in range(prev_x-x): # Left
                path = '<' + path

        if (prev_y < y): # Down
            for i in range(y-prev_y):
                path = 'v' + path
        else:
            for i in range(prev_y-y): # Up
                path = '^' + path

        curr = back_track[curr]
    if (end == (0,1) and start == (2,0)):
        print(path)
    print('\n')
    return path


def get_best_path(start, end, maze):
    queue = []
    seen_to_cost = {}
    
    heapq.heappush(queue, (0+get_manhattan_dist(start, end), start[0], start[1], 0))
    seen_to_cost[start] = 0
    back_track = {start: None}

    while len(queue) > 0:
        (cost_est, x, y, cost) = heapq.heappop(queue)
        if (x,y) == end:
            break
        neighbors = get_neighbors(x, y, maze)
        for n in neighbors:
            new_cost = cost + 1
            if n not in seen_to_cost or seen_to_cost[n] > new_cost:
                seen_to_cost[n] = new_cost
                heapq.heappush(queue, (new_cost+get_manhattan_dist(n, end), n[0], n[1], new_cost))
                back_track[n] = (x,y)

    curr = end
    path = ''
    while back_track[curr] != None:
        path += get_direction(back_track[curr], curr)
        curr = back_track[curr]

    return path

def get_instructions(line, locations, paths):
    instructions = ''
    for i in range(len(line)):
        start = locations['A']
        if i > 0:
            start = locations[line[i-1]]
        end = locations[line[i]]
        # print("instruct", start, end)
        
        if start != end:
            instructions += paths[start][end] + 'A'
        else:
            instructions += 'A'
    return instructions

def solve_day21_puzzle1():
    numeric_key_pad = [['7','8','9'], ['4','5','6'], ['1','2','3'], ['#','0','A']]
    numeric_paths = {}
    numeric_locations = {}
    for y in range(len(numeric_key_pad)):
        for x in range(len(numeric_key_pad[0])):
            if numeric_key_pad[y][x] == '#':
                continue
            start = (x,y)
            numeric_locations[numeric_key_pad[y][x]] = start
            for i in range(len(numeric_key_pad)):
                for j in range(len(numeric_key_pad[0])):
                    if numeric_key_pad[i][j] == '#' or (i == y and j == x):
                        continue
                    end = (j,i)
                    if start not in numeric_paths:
                        numeric_paths[start] = {}
                    numeric_paths[start][end]= ''


    # print(numeric_paths)
    # print(numeric_locations)

    directional_key_pad = [['#','^','A'],['<','v','>']]
    directional_paths = {}
    directional_locations = {}
    for y in range(len(directional_key_pad)):
        for x in range(len(directional_key_pad[0])):
            if directional_key_pad[y][x] == '#':
                continue
            start = (x,y)
            directional_locations[directional_key_pad[y][x]] = start
            for i in range(len(directional_key_pad)):
                for j in range(len(directional_key_pad[0])):
                    if directional_key_pad[i][j] == '#' or (i == y and j == x):
                        continue
                    end = (j,i)
                    if start not in directional_paths:
                        directional_paths[start] = {}
                    directional_paths[start][end] = ''

    # print(directional_paths)
    # print(directional_locations)

    for start in numeric_paths:
        for end in numeric_paths[start]:
            path = get_best_path_minimal_turns(start, end, numeric_key_pad)
            # print(start, end, path)
            numeric_paths[start][end] = path

    # print('\n')

    for start in directional_paths:
        for end in directional_paths[start]:
            path = get_best_path_minimal_turns(start, end, directional_key_pad)
            # print(start, end, path)
            directional_paths[start][end] = path

    f = open("inputs/test-day-21.txt", "r")

    complexities_sum = 0
    for line in f:
        line = line.strip()
        num = int(re.sub("\D", "", line))

        numeric_instructions = get_instructions(line, numeric_locations, numeric_paths)
        print("n", numeric_instructions)
        directional_instructions1 = get_instructions(numeric_instructions, directional_locations, directional_paths)
        print("d1", directional_instructions1)
        directional_instructions2 = get_instructions(directional_instructions1, directional_locations, directional_paths)
        print("d2", directional_instructions2)
        print(len(directional_instructions2), num)
        complexities_sum += num * len(directional_instructions2)

    f.close()
    return complexities_sum

print(solve_day21_puzzle1())