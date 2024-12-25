from enum import Enum
import heapq

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

def print_map(map):
    for y in range(len(map)):
        row = ''
        for x in range(len(map[0])):
            row += map[y][x].val
        print(row)

def get_best_path_coords():
    f = open('inputs/day-16.txt', 'r')

    maze = []
    line_idx = 0
    start = (0,0)
    end = (0,0)

    for line in f:
        maze.append([])
        line = line.strip()
        for i in range(len(line)):
            if line[i] == 'S':
                start = (i, line_idx)
            elif line[i] == 'E':
                end = (i, line_idx)
            maze[line_idx].append(line[i])
        line_idx += 1
    f.close()

    queue = []
    seen = set()
    directions = [Direction.RIGHT, Direction.UP, Direction.LEFT, Direction.DOWN]
    min_score = None
    dists = {}

    heapq.heappush(queue, (0, start[0], start[1], 0))
    while len(queue) > 0:
        (curr_dist, curr_x, curr_y, curr_dir_idx) = heapq.heappop(queue)
        if (curr_x, curr_y, curr_dir_idx) not in dists:
            dists[(curr_x, curr_y, curr_dir_idx)] = curr_dist

        if (curr_x, curr_y) == end:
            min_score = curr_dist
            break
        if (curr_x, curr_y, curr_dir_idx) not in seen:
            seen.add((curr_x, curr_y, curr_dir_idx))

            # Try to go in the same direction it's already in
            (curr_dir_x, curr_dir_y) = directions[curr_dir_idx].value
            (new_x, new_y) = (curr_x + curr_dir_x, curr_y + curr_dir_y)
            if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != '#':
                heapq.heappush(queue, (1+curr_dist, new_x, new_y, curr_dir_idx))

            # Add the neighbors you'd need a clockwise and counterclockwise turn for
            clockwise = curr_dir_idx-1 if curr_dir_idx-1 >= 0 else len(directions)-1
            counterclock = curr_dir_idx+1 if curr_dir_idx+1 < len(directions) else 0
            heapq.heappush(queue, (1000+curr_dist, curr_x, curr_y, clockwise))
            heapq.heappush(queue, (1000+curr_dist, curr_x, curr_y, counterclock))


    queue = []
    seen = set()
    dists2 = {}
    for i in range(len(directions)):
        heapq.heappush(queue, (0, end[0], end[1], i))

    while len(queue) > 0:
        (curr_dist, curr_x, curr_y, curr_dir_idx) = heapq.heappop(queue)

        op_direction_idx = curr_dir_idx - 2
        if op_direction_idx < 0:
            op_direction_idx = 4 + op_direction_idx
        if (curr_x, curr_y, op_direction_idx) not in dists2:
            dists2[(curr_x, curr_y, op_direction_idx)] = curr_dist

        if (curr_x, curr_y, curr_dir_idx) not in seen:
            seen.add((curr_x, curr_y, curr_dir_idx))

            # Try to go in the same direction it's already in
            (curr_dir_x, curr_dir_y) = directions[curr_dir_idx].value
            (new_x, new_y) = (curr_x + curr_dir_x, curr_y + curr_dir_y)
            if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != '#':
                heapq.heappush(queue, (1+curr_dist, new_x, new_y, curr_dir_idx))

            # Add the neighbors you'd need a clockwise and counterclockwise turn for
            clockwise = curr_dir_idx-1 if curr_dir_idx-1 >= 0 else len(directions)-1
            counterclock = curr_dir_idx+1 if curr_dir_idx+1 < len(directions) else 0
            heapq.heappush(queue, (1000+curr_dist, curr_x, curr_y, clockwise))
            heapq.heappush(queue, (1000+curr_dist, curr_x, curr_y, counterclock))


    coords = set()
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            for i in range(len(directions)):
                if (x,y,i) in dists and (x,y,i) in dists2 and dists[(x,y,i)] + dists2[(x,y,i)] == min_score:
                    coords.add((x,y))

    return coords

def solve_day16_puzzle2():
    best_path_coords = get_best_path_coords()
    return len(best_path_coords)


print(solve_day16_puzzle2())
