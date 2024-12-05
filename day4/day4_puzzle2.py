def solve_day4_puzzle2():
    puzzle = []
    a_locations = []
    line_num = 0

    f = open("inputs/day-4.txt", "r")
    for line in f:

        for j in range(len(line)):
            if line[j] == 'A':
                a_locations.append((line_num, j))

        puzzle.append(line)
        line_num += 1

    f.close()

    count = 0
    for loc in a_locations:
        line_i = loc[0]
        char_i = loc[1]

        if check_for_xmas(puzzle, line_i, char_i):
            count += 1

    return count


def check_for_xmas(puzzle, line_i, char_i):
    if (line_i-1 >= 0 and line_i+1 <= len(puzzle)-1 and char_i-1 >= 0 and char_i+1 <= len(puzzle[0])-2):
        upper_left = puzzle[line_i-1][char_i-1]
        upper_right = puzzle[line_i-1][char_i+1]

        lower_left = puzzle[line_i+1][char_i-1]
        lower_right = puzzle[line_i+1][char_i+1]

        if upper_left == 'M' and lower_right == 'S':
            if (lower_left == 'M' and upper_right == 'S') or  (lower_left == 'S' and upper_right == 'M'):
                return True
        elif upper_left == 'S' and lower_right == 'M':
            if (lower_left == 'M' and upper_right == 'S') or  (lower_left == 'S' and upper_right == 'M'):
                return True
        
    return False


print(solve_day4_puzzle2())