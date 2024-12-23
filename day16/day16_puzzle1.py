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


def get_neighbors(x, y, map):
    neighbors =[]
    if check_in_bounds(x, y-1, map):
        neighbors.append((map[y-1][x], Direction.UP))
    if check_in_bounds(x-1, y, map):
        neighbors.append((map[y][x-1], Direction.LEFT))
    if check_in_bounds(x+1, y, map):
        neighbors.append((map[y][x+1], Direction.RIGHT))
    if check_in_bounds(x, y+1, map):
        neighbors.append((map[y+1][x], Direction.DOWN))

    return neighbors


def print_neighbors(neighbors):
    for n in neighbors:
        print(n[0].x, n[0].y, n[0].val)


def check_in_bounds(x, y, map):
    if (x >= 0 and x <= len(map[0])-1 and y >= 0 and y <= len(map)-1) and map[y][x].val != '#' and map[y][x].val != 'S':
        return True
    else:
        return False
    

def relax(curr, neighbor, queue):
    (n, n_direction) = neighbor
    w = get_weight(n_direction, curr.direction)
    if (curr.dist + w < n.dist):
        n.dist = curr.dist + w
        n.prev = curr
        n.direction = n_direction
        queue.add_task(n, n.dist)


def get_weight(n_direction, curr_direction):
    if (n_direction == curr_direction):
        return 1
    else:
        if n_direction == Direction.UP or n_direction == Direction.DOWN:
            if curr_direction == Direction.LEFT or curr_direction == Direction.RIGHT:
                return 1 + 1000
            else: 
                return 1 + 2 * 1000
        elif n_direction == Direction.LEFT or n_direction == Direction.RIGHT:
            if curr_direction == Direction.UP or curr_direction == Direction.DOWN:
                return 1 + 1000
            else: 
                return 1 + 2 * 1000
    return


def solve_day16_puzzle1():
    f = open('inputs/test-4-day-16.txt', 'r')

    map = []
    line_idx = 0
    end = None

    queue = PriorityQueue()

    for line in f:
        map.append([])
        line = line.strip()
        for i in range(len(line)):
            v = Vertex(i, line_idx, line[i], Direction.RIGHT)
            if line[i] == 'S':
                v.dist = 0
            elif line[i] == 'E':
                end = v

            if line[i] != '#':
                queue.add_task(v, v.dist)
            map[line_idx].append(v)
        line_idx += 1
    f.close()

    while queue.length > 0:
        curr = queue.pop_task()
        neighbors = get_neighbors(curr.x, curr.y, map)
        for n in neighbors:
            relax(curr, n, queue)
            
    return end.dist


print(solve_day16_puzzle1())
