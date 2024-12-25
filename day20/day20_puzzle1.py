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


def get_possible_cheat_locations(maze):
    possible_cheat_coords = []
    for y in range(1,len(maze)-1):
        for x in range(1,len(maze[0])-1):
            if maze[y][x] == '#':
                possible_cheat_coords.append((x,y))
    return possible_cheat_coords
                    

def get_end_time(start, end, maze):
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

    steps = 0
    curr = end
    while back_track[curr] != None:
        curr = back_track[curr]
        steps += 1

    return steps


def solve_day20_puzzle1():
    f = open("inputs/day-20.txt", "r")

    maze = []

    start = (0,0)
    end = (0,0)

    line_idx = 0

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

    picoseconds_without_cheats = get_end_time(start, end, maze)
    picoseconds_to_save = 100

    print(picoseconds_without_cheats)

    best_cheats = 0
    # best_cheats_map = {}
    possible_cheats = get_possible_cheat_locations(maze)
    i = 0
    for cheat in possible_cheats:
        print(cheat)
        (x, y) = cheat
        maze[y][x] = '.'
        picoseconds = get_end_time(start, end, maze)

        # This is used for testing the example
        # picoseconds_saved = picoseconds_without_cheats - picoseconds
        # if picoseconds_saved in best_cheats_map:
        #     best_cheats_map[picoseconds_saved] += 1
        # else:
        #     best_cheats_map[picoseconds_saved] = 1

        if picoseconds <= picoseconds_without_cheats - picoseconds_to_save:
            best_cheats += 1
        maze[y][x] = '#'
        i += 1

    # print(best_cheats_map)
    return best_cheats
    

print(solve_day20_puzzle1())