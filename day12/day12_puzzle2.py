
def solve_day12_puzzle2():
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

    top = {}
    bottom = {}
    left = {}
    right = {}

    for y in range(len(map)):
        for x in range(len(map[0])):
            if not (x, y) in visited:
                to_visit.append((x,y))
                if curr_letter == None:
                    # Make a new region
                    curr_letter = map[y][x]
                    regions.append([0, 0])
                    region_i += 1

                    if region_i-1 >= 0:
                        # Add the sides up for the previous region
                        regions[region_i-1][1] = count_sides(top) + count_sides(bottom) + count_sides(left) + count_sides(right)
                        # Clear out the dictionaries to start the counts for the new current region
                        top.clear()
                        bottom.clear()
                        left.clear()
                        right.clear()

                while len(to_visit) > 0:
                    (curr_x, curr_y) = to_visit.pop()
                    if not (curr_x, curr_y) in visited:
                        visited.add((curr_x, curr_y))
                        regions[region_i][0] += 1

                        neighbors = get_neighbors(curr_x, curr_y)
                        for n in neighbors:
                            (nx, ny) = n
                            if (check_in_bounds(nx, ny, map)):
                                if map[ny][nx] == curr_letter:
                                    to_visit.append(n)
                                else:
                                    if (curr_y - 1) == ny: 
                                        add_to_sides_dict(curr_x, curr_y, top)
                                    if (curr_y + 1) == ny: 
                                        add_to_sides_dict(curr_x, curr_y, bottom)
                                    if (curr_x - 1) == nx: 
                                        add_to_sides_dict(curr_y, curr_x, left)
                                    if (curr_x + 1) == nx: 
                                        add_to_sides_dict(curr_y, curr_x, right)
                            else:
                                if curr_y - 1 < 0:
                                    add_to_sides_dict(curr_x, curr_y, top)
                                if curr_y + 1 > len(map) - 1:
                                    add_to_sides_dict(curr_x, curr_y, bottom)
                                if curr_x - 1 < 0:
                                    add_to_sides_dict(curr_y, curr_x, left)
                                if curr_x + 1 > len(map[0]) - 1:
                                    add_to_sides_dict(curr_y, curr_x, right)
            curr_letter = None
        
    # Count up the sides for the last region
    regions[region_i][1] = count_sides(top) + count_sides(bottom) + count_sides(left) + count_sides(right)

    # Use the area and the number of sides to calc the total price
    total = 0
    for region in regions:
        total += region[0] * region[1]
        
    return total


def count_sides(side_dict):
    side_count = 0
    for idx in side_dict:
        side_count += len(side_dict[idx])
    return side_count

# Note that for left and right sides, curr_x will actually be a y value and curr_y will actually be an x.
# I should rename these, to be more clear, but I am leaving it like this for now.
def add_to_sides_dict(curr_x, curr_y, side_dict):
    if not curr_y in side_dict:
        side_dict[curr_y] = []
    # Create a new side if there are no prexisiting sides to see if you can add the curr_x to.
    if len(side_dict[curr_y]) == 0:
        side_dict[curr_y].append([curr_x, curr_x])
    # Check if you should add the curr_x to a prexisting side or add a new side.
    else:
        inserted = False
        beginnings = {}
        ends = {}
        segment_changed_idx = None

        for i in range(len(side_dict[curr_y])):
            # These lines make it easier to access the upper and lower bounds.
            segments = side_dict[curr_y][i]
            lower_bound = segments[0]
            upper_bound = segments[1]

            # Keep track of all the upper and lower bounds and at what index in side_dict[curr_y] they occur.
            beginnings[lower_bound] = i
            ends[upper_bound] = i

            # If the curr_x was already inserted, we don't need to check to add it again.
            # We only need to do the part above to keep track of all the upper and lower bonds for the side_dict.
            if not inserted:
                # Case of the curr_x already being in a side
                if (curr_x == lower_bound or curr_x == upper_bound):
                    inserted = True

                # Case of adding to the left of a prexisting side
                elif (curr_x == lower_bound - 1):
                    inserted = True
                    # Update beginnings
                    beginnings.pop(segments[0])
                    beginnings[curr_x] = i
                    # Change the lower bound of the segment to be the curr_x
                    segments[0] = curr_x
                    segment_changed_idx = i
                    
                # Case of adding to the right of a prexisting side
                elif (curr_x == upper_bound + 1):
                    inserted = True
                    # Update ends
                    ends.pop(segments[1])
                    ends[curr_x] = i
                    # Change the upper bound of the segment to be the curr_x
                    segments[1] = curr_x
                    segment_changed_idx = i

        if not inserted:
            # The curr_x was not able to extend a prexisting side. Create a new side.
            side_dict[curr_y].append([curr_x, curr_x])
        else:
            # See if inserting curr_x has makes the side it was inserted into connect with another prexisting side.
            if (curr_x - 1 in ends):
                side_dict[curr_y][segment_changed_idx][0] = side_dict[curr_y][ends[curr_x - 1]][0]
                side_dict[curr_y].pop(ends[curr_x - 1])
            elif (curr_x + 1 in beginnings):
                side_dict[curr_y][segment_changed_idx][1] = side_dict[curr_y][beginnings[curr_x + 1]][1]
                side_dict[curr_y].pop(beginnings[curr_x + 1])


def get_neighbors(x, y):
    neighbors =[]
    neighbors.append((x-1, y))
    neighbors.append((x, y-1))
    neighbors.append((x+1, y))
    neighbors.append((x, y+1))
    return neighbors


def check_in_bounds(x, y, map):
    if (x >= 0 and x <= len(map[0])-1 and y >= 0 and y <= len(map)-1):
        return True
    else:
        return False


print(solve_day12_puzzle2())