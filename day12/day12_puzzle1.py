def solve_day12_puzzle1():
    f = open("inputs/test-day-12.txt", "r")

    map = []

    for line in f:
        map.append(line.strip())       
    f.close()

    visited = set()
    to_visit = []
    regions = {}
    r_list = {}

    curr_letter = None
    for y in range(len(map)):
        for x in range(len(map[0])):
            if not (x, y) in visited:
                if not curr_letter:
                    curr_letter = map[y][x]
                    regions[curr_letter] = [0, 0]
                to_visit.append((x,y))
                r_list[curr_letter] = []

                while len(to_visit) > 0:
                    (curr_x, curr_y) = to_visit.pop()
                    if not (curr_x, curr_y) in visited:
                        r_list[curr_letter].append((curr_x, curr_y))
                        visited.add((curr_x, curr_y))
                        if len(r_list[curr_letter]) == 1:
                            regions[curr_letter] = [1, 4]
                        else:
                            regions[curr_letter][0] += 1
                            regions[curr_letter][1] += 4 - 2

                        neighbors = get_neighbors(curr_x, curr_y, map)
                        for n in neighbors:
                            (nx, ny) = n
                            if map[ny][nx] == curr_letter:
                                to_visit.append(n)
            curr_letter = None

    total = 0
    for letter in regions:
        print(regions[letter])
        
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