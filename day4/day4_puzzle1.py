def solve_day4_puzzle1():
    puzzle = []
    x_locations = []
    line_num = 0

    f = open("inputs/day-4.txt", "r")
    for line in f:

        for j in range(len(line)):
            if line[j] == 'X':
                x_locations.append((line_num, j))

        puzzle.append(line)
        line_num += 1

    f.close()

    count = 0
    for loc in x_locations:
        line_i = loc[0]
        char_i = loc[1]

        count += count_matches_around(puzzle, line_i, char_i)

    return count

def count_matches_around(puzzle, line_i, char_i):
    upper_left = check_for_match(puzzle, line_i, char_i, -1, -1)
    above = check_for_match(puzzle, line_i, char_i, -1, 0)
    upper_right = check_for_match(puzzle, line_i, char_i, -1, 1)

    left = check_for_match(puzzle, line_i, char_i, 0, -1)
    right = check_for_match(puzzle, line_i, char_i, 0, 1)

    lower_left = check_for_match(puzzle, line_i, char_i, 1, -1)
    below = check_for_match(puzzle, line_i, char_i, 1, 0)
    lower_right = check_for_match(puzzle, line_i, char_i, 1, 1)

    count = 0

    if upper_left:
        count += 1
    if above:
        count += 1
    if upper_right:
        count += 1
    if left:
        count += 1
    if right:
        count += 1
    if lower_left:
        count += 1
    if below:
        count += 1
    if lower_right:
        count += 1

    return count


def check_for_match(puzzle, line_i, char_i, line_diff, char_diff):
    if check_for_neighbor_letter('M', puzzle, line_i, char_i, line_diff, char_diff):
        line_i = line_i + line_diff
        char_i = char_i + char_diff
        if check_for_neighbor_letter('A', puzzle, line_i, char_i, line_diff, char_diff):
            line_i = line_i + line_diff
            char_i = char_i + char_diff
            if check_for_neighbor_letter('S', puzzle, line_i, char_i, line_diff, char_diff):
                return True
            
    return False


def check_for_neighbor_letter(letter, puzzle, line_i, char_i, line_diff, char_diff):
    new_line_i = line_i + line_diff
    new_char_i = char_i + char_diff


    if (new_line_i >= 0 and new_char_i >= 0 and new_line_i < len(puzzle) and new_char_i < len(puzzle[0])-1):
        neighbor = puzzle[new_line_i][new_char_i]
        if neighbor == letter:
            return True
        else:
            return False
    else:
        return False


print(solve_day4_puzzle1())