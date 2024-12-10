def solve_day10_puzzle1():
    f = open("inputs/day-10.txt", "r")
    
    map = []
    trailheads = {}
    line_idx = 0

    stack = []

    # build the map and find all the trailheads
    for line in f:
        map.append(line.strip())
        for i in range(len(line)):
            if line[i] == '0':
                coords = (i, line_idx, 0)
                stack.append(coords)
                trailheads[coords] = []
        line_idx += 1
    f.close()

    sum = 0
    curr_trailhead = None
    while len(stack) > 0:
        (char_i, line_i, number) = stack.pop()
        if (number == 0):
            curr_trailhead = trailheads[(char_i, line_i, number)]

        # above
        check_for_next_step(number + 1, map, line_i, char_i, -1, 0, curr_trailhead, stack)
        # left
        check_for_next_step(number + 1, map, line_i, char_i, 0, -1, curr_trailhead, stack)
        # right
        check_for_next_step(number + 1, map, line_i, char_i, 0, 1, curr_trailhead, stack)
        # below
        check_for_next_step(number + 1, map, line_i, char_i, 1, 0, curr_trailhead, stack)

    for v in trailheads.values():
        sum += len(v)

    return sum


def check_for_next_step(next_number, map, line_i, char_i, line_diff, char_diff, curr_trailhead, stack):
    new_line_i = line_i + line_diff
    new_char_i = char_i + char_diff

    if (new_line_i >= 0 and new_char_i >= 0 and new_line_i <= len(map)-1 and new_char_i <= len(map[0])-1):
        neighbor = map[new_line_i][new_char_i]
        if int(neighbor) == int(next_number):
            if (next_number == 9):
                curr_trailhead.append((new_char_i, new_line_i))
            else:
                stack.append((new_char_i, new_line_i, next_number))


print(solve_day10_puzzle1())