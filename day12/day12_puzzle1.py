def solve_day12_puzzle1():
    f = open("inputs/day-12.txt", "r")

    map = []

    for line in f:
        map.append(line.strip())       
    f.close()

    visited = set()
    to_visit = []
    regions = []
    region_i = -1

    curr_letter = None
    for y in range(len(map)):
        for x in range(len(map[0])):
            if not (x, y) in visited:
                if curr_letter == None:
                    curr_letter = map[y][x]
                    regions.append([0, 0])
                    region_i += 1
                to_visit.append((x,y))

                while len(to_visit) > 0:
                    (curr_x, curr_y) = to_visit.pop()
                    if not (curr_x, curr_y) in visited:
                        visited.add((curr_x, curr_y))
                        # add to the area
                        regions[region_i][0] += 1

                        num_neighbors_in_same_region = 0
                        neighbors = get_neighbors(curr_x, curr_y, map)
                        for n in neighbors:
                            (nx, ny) = n
                            if map[ny][nx] == curr_letter:
                                num_neighbors_in_same_region += 1
                                to_visit.append(n)
                        # add to the perimeter
                        regions[region_i][1] += 4 - num_neighbors_in_same_region
            curr_letter = None

    total = 0
    for region in regions:
        total += region[0] * region[1]
        
    return total


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


def check_in_bounds(x, y, map):
    if (x >= 0 and x <= len(map[0])-1 and y >= 0 and y <= len(map)-1):
        return True
    else:
        return False


print(solve_day12_puzzle1())