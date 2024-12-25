from collections import deque
import heapq


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


def solve_day18_puzzle1(grid_width, bytes_fallen, file_name):
    f = open(file_name, "r")

    grid = []
    for y in range(grid_width):
        grid.append([])
        for x in range(grid_width):
            grid[-1].append(".")

    byte_num = 0
    for line in f:
        if byte_num < bytes_fallen:
            split_line = line.split(',')
            x = int(split_line[0])
            y = int(split_line[1])
            grid[y][x] = '#'

            byte_num += 1
        else:
            break

    f.close()

    start = (0,0)
    end = (grid_width-1, grid_width-1)

    queue = []
    seen_to_cost = {}
    heapq.heappush(queue, (0+get_manhattan_dist(start, end), start[0], start[1], 0))
    seen_to_cost[start] = 0
    back_track = {start: None}

    print(start)
    print(end)
    print(grid)
    print('\n')

    while len(queue) > 0:
        (cost_est, x, y, cost) = heapq.heappop(queue)
        if (x,y) == end:
            break
        neighbors = get_neighbors(x, y, grid)
        for n in neighbors:
            new_cost = cost + 1
            if n not in seen_to_cost or seen_to_cost[n] > new_cost:
                seen_to_cost[n] = new_cost
                heapq.heappush(queue, (new_cost+get_manhattan_dist(n, end), n[0], n[1], new_cost))
                back_track[n] = (x,y)

    steps = 0
    curr = (grid_width-1, grid_width-1)
    while back_track[curr] != None:
        (x,y) = back_track[curr]
        grid[y][x] = 'O'
        curr = back_track[curr]
        steps += 1

    print_map(grid)
    return steps


#print(solve_day18_puzzle1(7, 12, "inputs/test-day-18.txt"))
print(solve_day18_puzzle1(71, 1024, "inputs/day-18.txt"))