import itertools


def solve_day8_puzzle1():
    f = open("inputs/day-8.txt", "r")

    antinode_locations = set()
    map = []
    freq_and_locations = {}
    line_idx = 0

    for line in f:
        line = line.strip()
        map.append(line)
        for i in range(len(line)):
            c = line[i]
            if c != '.':
                if not c in freq_and_locations:
                    freq_and_locations[c] = []
                freq_and_locations[c].append((i, line_idx))

        line_idx += 1

    f.close()

    for freq in freq_and_locations:
        loc_list = freq_and_locations[freq]
        for i in range(len(loc_list)):
            for j in range(i+1, len(loc_list)):
                loc1 = loc_list[i]
                loc2 = loc_list[j]

                new_pos1 = get_new_pos(loc1, loc2)
                new_pos2 = get_new_pos(loc2, loc1)

                if check_in_range(new_pos1, map):
                    antinode_locations.add(new_pos1)

                if check_in_range(new_pos2, map):
                    antinode_locations.add(new_pos2)

    return len(antinode_locations)


def get_new_pos(loc1, loc2):
    dx = loc2[0] - loc1[0]
    dy = loc2[1] - loc1[1]
    new_pos = (loc2[0] + dx, loc2[1] + dy)
    return new_pos


def check_in_range(next_pos, map):
    if next_pos[0] >= 0 and next_pos[0] <= len(map[0]) - 1 and next_pos[1] >= 0 and next_pos[1] <= len(map) - 1:
        return True
    else:
        return False


print(solve_day8_puzzle1())