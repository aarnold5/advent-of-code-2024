from collections import deque
from enum import Enum
import itertools
from numpy import Infinity
import heapq

# from https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes
class PriorityQueue:
    pq = []                         # list of entries arranged in a heap
    entry_finder = {}               # mapping of tasks to entries
    REMOVED = '<removed-task>'      # placeholder for a removed task
    counter = itertools.count()     # unique sequence count
    length = 0

    def add_task(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        else:
            self.length += 1
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                self.length -= 1
                return task
        raise KeyError('pop from an empty priority queue')


class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)


class Vertex:
    x = 0
    y = 0
    val = '.'
    direction: None
    dist = Infinity
    prev = None

    def __init__(self, x, y, val, direction):
        self.x = x
        self.y = y
        self.val = val
        self.direction = direction


def print_map(map):
    for y in range(len(map)):
        row = ''
        for x in range(len(map[0])):
            row += map[y][x].val
        print(row)


def get_neighbors(x, y, map, start_symbol):
    neighbors =[]
    if check_in_bounds(x, y-1, map, start_symbol):
        neighbors.append((map[y-1][x], Direction.UP))
    if check_in_bounds(x-1, y, map, start_symbol):
        neighbors.append((map[y][x-1], Direction.LEFT))
    if check_in_bounds(x+1, y, map, start_symbol):
        neighbors.append((map[y][x+1], Direction.RIGHT))
    if check_in_bounds(x, y+1, map, start_symbol):
        neighbors.append((map[y+1][x], Direction.DOWN))

    return neighbors


def print_neighbors(neighbors):
    for n in neighbors:
        print(n[0].x, n[0].y, n[0].val)


def check_in_bounds(x, y, map, start_symbol):
    if (x >= 0 and x <= len(map[0])-1 and y >= 0 and y <= len(map)-1) and map[y][x].val != '#' and map[y][x].val != start_symbol:
        return True
    else:
        return False
    

def check_if_check(x, y, map, coords_on_path):
    if (x >= 0 and x <= len(map[0])-1 and y >= 0 and y <= len(map)-1) and map[y][x].val != '#' and map[y][x].val != 'E' and ((x,y) not in coords_on_path):
        return True
    else:
        return False
    

def relax(curr, neighbor, queue):
    (n, n_direction) = neighbor
    w = get_weight(n_direction, curr.direction, curr.val)
    if (curr.dist + w < n.dist):
        n.dist = curr.dist + w
        n.prev = curr
        n.direction = n_direction
        queue.add_task(n, n.dist)


def get_weight(n_direction, curr_direction, curr_val):
    if (n_direction == curr_direction or curr_val == 'E'):
        return 1
    else:
        if n_direction == Direction.UP or n_direction == Direction.DOWN:
            if curr_direction == Direction.LEFT or curr_direction == Direction.RIGHT:
                return 1 + 1000
            else: 
                return 0
        elif n_direction == Direction.LEFT or n_direction == Direction.RIGHT:
            if curr_direction == Direction.UP or curr_direction == Direction.DOWN:
                return 1 + 1000
            else: 
                return 0
    return


def get_path(end):
    curr = end
    path = [end]
    coords_on_path = set()
    coords_on_path.add((end.x, end.y))
    while curr.prev != None:
        path.append(curr.prev)
        coords_on_path.add((curr.prev.x, curr.prev.y))
        curr = curr.prev

    return (path, coords_on_path)


def get_score(start_symbol, end_symbol, alt_start_v = None):
    f = open('inputs/test-day-16.txt', 'r')

    map = []
    line_idx = 0
    end = None

    queue = PriorityQueue()

    for line in f:
        map.append([])
        line = line.strip()
        for i in range(len(line)):
            v = Vertex(i, line_idx, line[i], Direction.RIGHT)
            if line[i] == start_symbol and alt_start_v == None:
                v.dist = 0
            elif alt_start_v != None and (alt_start_v.x, alt_start_v.y) == (i, line_idx):
                v = alt_start_v
                v.val = "X"
                start_symbol = 'X'
            elif line[i] == end_symbol:
                end = v

            if line[i] != '#':
                queue.add_task(v, v.dist)
            map[line_idx].append(v)
        line_idx += 1
    f.close()

    while queue.length > 0:
        curr = queue.pop_task()
        if curr.val == end_symbol:
            break
        neighbors = get_neighbors(curr.x, curr.y, map, start_symbol)
        for n in neighbors:
            if n != curr.prev:
                relax(curr, n, queue)

    if end.val == 'S':
        if end.direction == Direction.DOWN or end.direction == Direction.UP:
            end.dist += 1000

    (path, coords_on_path) = get_path(end)
            
    return (end.dist, path, coords_on_path, map)


def solve_day16_puzzle1():
    (s_to_e_score, s_to_e_path, s_to_e_coords, s_to_e_map) = get_score('S', 'E')
    (e_to_s_score, e_to_s_path, e_to_s_coords, e_to_s_map) = get_score('E', 'S')

    if s_to_e_score < e_to_s_score:
        to_check = set()
        for i in range(len(s_to_e_path)):
            v_prev_direction = Direction.RIGHT
            v = s_to_e_path[i]
            # print(v.val)
            if (v.val != 'S') and (v.val != 'E') :
                v_prev = s_to_e_path[i-1]
                if v_prev.y - 1 == v.y:
                    v_prev_direction = Direction.UP
                elif v_prev.y + 1 == v.y:
                    v_prev_direction = Direction.DOWN
                elif v_prev.x + 1 == v.x:
                    v_prev_direction = Direction.RIGHT
                elif v_prev.x - 1 == v.x:
                    v_prev_direction = Direction.LEFT
                
            if v.val != 'S' and v.prev.val != 'S':
                # need to adjust the directions and the scores based of if there is a direction change or not for these paths
                if check_if_check(v.x, v.y-1, s_to_e_map, s_to_e_coords):
                    # print((v.x, v.y-1, Direction.UP, v_prev_direction))
                    new_start = s_to_e_map[v.y-1][v.x]
                    new_start.direction = Direction.UP
                    new_start.dist = new_start.dist + get_weight(new_start.direction, v_prev_direction, '')
                    to_check.add(new_start)
                elif check_if_check(v.x-1, v.y, s_to_e_map, s_to_e_coords):
                    # print((v.x-1, v.y, Direction.LEFT, v_prev_direction))
                    new_start = s_to_e_map[v.y][v.x-1]
                    new_start.direction = Direction.LEFT
                    new_start.dist = new_start.dist + get_weight(new_start.direction, v_prev_direction, '')
                    to_check.add(new_start)
                elif check_if_check(v.x+1, v.y, s_to_e_map, s_to_e_coords):
                    # print((v.x+1, v.y, Direction.RIGHT, v_prev_direction))
                    new_start = s_to_e_map[v.y][v.x+1]
                    new_start.direction = Direction.RIGHT
                    new_start.dist = new_start.dist + get_weight(new_start.direction, v_prev_direction, '')
                    to_check.add(new_start)
                elif check_if_check(v.x, v.y+1, s_to_e_map, s_to_e_coords):
                    # print((v.x, v.y+1, Direction.DOWN, v_prev_direction))
                    new_start = s_to_e_map[v.y+1][v.x]
                    new_start.direction = Direction.DOWN
                    new_start.dist = new_start.dist + get_weight(new_start.direction, v_prev_direction, '')
                    to_check.add(new_start)

        for alt_start in to_check:
            print("testing ", alt_start.x, alt_start.y)
            (alt_s_to_e_score, alt_s_to_e_path, alt_s_to_e_coords, alt_s_to_e_map) = get_score('E', 'S', alt_start)
            if alt_s_to_e_score == s_to_e_score:
                print(alt_s_to_e_score)
                for coord in alt_s_to_e_coords:
                    print(coord)
                    s_to_e_coords.add(coord)

        

        print('\n') 

        i = 0
        for item in s_to_e_coords:
            print(i, item)
            i+=1
        print(len(s_to_e_coords))
    else:
        to_check = set()
        for i in range(len(e_to_s_path)):
            v_prev_direction = Direction.RIGHT
            v = e_to_s_path[i]
            # print(v.val)
            if (v.val != 'S') and (v.val != 'E') :
                v_prev = e_to_s_path[i-1]
                if v_prev.y - 1 == v.y:
                    v_prev_direction = Direction.UP
                elif v_prev.y + 1 == v.y:
                    v_prev_direction = Direction.DOWN
                elif v_prev.x + 1 == v.x:
                    v_prev_direction = Direction.RIGHT
                elif v_prev.x - 1 == v.x:
                    v_prev_direction = Direction.LEFT
                
            if v.val != 'E' and v.prev.val != 'E':
                # need to adjust the directions and the scores based of if there is a direction change or not for these paths
                if check_if_check(v.x, v.y-1, e_to_s_map, e_to_s_coords):
                    # print((v.x, v.y-1, Direction.UP, v_prev_direction))
                    new_start = e_to_s_map[v.y-1][v.x]
                    new_start.direction = Direction.UP
                    new_start.dist = new_start.dist + get_weight(new_start.direction, v_prev_direction, '')
                    to_check.add(new_start)
                elif check_if_check(v.x-1, v.y, e_to_s_map, e_to_s_coords):
                    # print((v.x-1, v.y, Direction.LEFT, v_prev_direction))
                    new_start = e_to_s_map[v.y][v.x-1]
                    new_start.direction = Direction.LEFT
                    new_start.dist = new_start.dist + get_weight(new_start.direction, v_prev_direction, '')
                    to_check.add(new_start)
                elif check_if_check(v.x+1, v.y, e_to_s_map, e_to_s_coords):
                    # print((v.x+1, v.y, Direction.RIGHT, v_prev_direction))
                    new_start = e_to_s_map[v.y][v.x+1]
                    new_start.direction = Direction.RIGHT
                    new_start.dist = new_start.dist + get_weight(new_start.direction, v_prev_direction, '')
                    to_check.add(new_start)
                elif check_if_check(v.x, v.y+1, e_to_s_map, e_to_s_coords):
                    # print((v.x, v.y+1, Direction.DOWN, v_prev_direction))
                    new_start = e_to_s_map[v.y+1][v.x]
                    new_start.direction = Direction.DOWN
                    new_start.dist = new_start.dist + get_weight(new_start.direction, v_prev_direction, '')
                    to_check.add(new_start)

        for alt_start in to_check:
            print("testing ", alt_start.x, alt_start.y)
            (alt_e_to_s_score, alt_e_to_s_path, alt_e_to_s_coords, alt_e_to_s_map) = get_score('E', 'S', alt_start)
            if alt_e_to_s_score == e_to_s_score:
                print(alt_e_to_s_score)
                for coord in alt_e_to_s_coords:
                    print(coord)
                    e_to_s_coords.add(coord)

        

        print('\n') 

        i = 0
        for item in e_to_s_coords:
            print(i, item)
            i+=1
        print(len(e_to_s_coords))
        # for v in to_check:
        #     print(v[0].x, v[0].y)
        
            

    return min(s_to_e_score, e_to_s_score)


print(solve_day16_puzzle1())
