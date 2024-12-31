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
                    

def get_picos_and_path(start, end, maze):
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
    path = [curr]
    while back_track[curr] != None:
        path.append(back_track[curr])
        curr = back_track[curr]

    return path


def solve_day20_puzzle2():
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

    path = get_picos_and_path(start, end, maze)
    picoseconds_to_save = 100

    num_cheats = 0
    for i in range(len(path)):
        print("testing path index " + str(i))
        coord1 = path[i]
        for j in range(len(path)):
            coord2 = path[j]

            if coord1 == coord2:
                continue
            
            straight_dist = get_manhattan_dist(coord1, coord2)
            path_dist = j - i

            picos_saved = path_dist - straight_dist

            if straight_dist <= 20 and picos_saved >= picoseconds_to_save:
                num_cheats += 1

    return num_cheats

print(solve_day20_puzzle2())