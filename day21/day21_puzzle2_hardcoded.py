import re


def print_map(map):
    for y in map:
        print(str(y)+'\n')
    

def get_instructions(line, paths):
    instructions = ''
    for i in range(len(line)):
        start = 'A'
        if i > 0:
            start = line[i-1]
        end = line[i]
        
        if start != end:
            instructions += paths[start][end] + 'A'
        else:
            instructions += 'A'
    return instructions


def dfs(line, path, seen_before, depth):
    if depth == 0:
        # print("end of branch", line, len(line))
        return len(line)
    
    if (line, depth) in seen_before:
        # print("found end of branch", line, len(line))
        return seen_before[(line, depth)]
    
    total = 0
    parts = line.split("A")
    # print(parts)
    for i in range(len(parts)):
        part = parts[i]
        if i != len(parts) - 1:
            part = part + 'A'
            instructions = get_instructions(part, path)
            # print(part, depth, instructions)
            total += dfs(instructions, path, seen_before, depth-1)
    seen_before[(line, depth)] = total
        
    return total


def solve_day21_puzzle1():

    best_numeric_paths = {
        '7': {
            '8': '>',
            '9': '>>',
            '4': 'v',
            '5': 'v>',
            '6': 'v>>',
            '1': 'vv',
            '2': 'vv>',
            '3': 'vv>>',
            '0': '>vvv',
            'A': '>>vvv',
        },
        '8': {
            '7': '<',
            '9': '>',
            '4': '<v',
            '5': 'v',
            '6': 'v>',
            '1': '<vv',
            '2': 'vv',
            '3': 'vv>',
            '0': 'vvv',
            'A': 'vvv>',
        },
        '9': {
            '7': '<<',
            '8': '<',
            '4': '<<v',
            '5': '<v',
            '6': 'v',
            '1': '<<vv',
            '2': '<vv',
            '3': 'vv',
            '0': '<vvv',
            'A': 'vvv',
        },
        '4': {
            '7': '^',
            '8': '^>',
            '9': '^>>',
            '5': '>',
            '6': '>>',
            '1': 'v',
            '2': 'v>',
            '3': 'v>>',
            '0': '>vv',
            'A': '>>vv',
        },
        '5': {
            '7': '<^',
            '8': '^',
            '9': '^>',
            '4': '<',
            '6': '>',
            '1': '<v',
            '2': 'v',
            '3': 'v>',
            '0': 'vv',
            'A': 'vv>',
        },
        '6': {
            '7': '<<^',
            '8': '<^',
            '9': '^',
            '4': '<<',
            '5': '<',
            '1': '<<v',
            '2': '<v',
            '3': 'v',
            '0': '<vv',
            'A': 'vv',
        },
        '1': {
            '7': '^^',
            '8': '^^>',
            '9': '^^>>',
            '4': '^',
            '5': '^>',
            '6': '^>>',
            '2': '>',
            '3': '>>',
            '0': '>v',
            'A': '>>v',
        },
        '2': {
            '7': '<^^',
            '8': '^^',
            '9': '^^>',
            '4': '<^',
            '5': '^',
            '6': '^>',
            '1': '<',
            '3': '>',
            '0': 'v',
            'A': 'v>',
        },
        '3': {
            '7': '<<^^',
            '8': '<^^',
            '9': '^^',
            '4': '<<^',
            '5': '<^',
            '6': '^',
            '1': '<<',
            '2': '<',
            '0': '<v',
            'A': 'v',
        },
        '0': {
            '7': '^^^<',
            '8': '^^^',
            '9': '^^^>',
            '4': '^^<',
            '5': '^^',
            '6': '^^>',
            '1': '^<',
            '2': '^',
            '3': '^>',
            'A': '>',
        },
        'A': {
            '7': '^^^<<', 
            '8': '<^^^',
            '9': '^^^',
            '4': '^^<<',
            '5': '<^^',
            '6': '^^',
            '1': '^<<',
            '2': '<^',
            '3': '^',
            '0': '<',
        },
    }

    best_direction_paths = {
        '^': {
            'A': '>',
            '<': 'v<',
            'v': 'v',
            '>': 'v>'
        },
        'A': {
            '^': '<',
            '<': 'v<<',
            'v': '<v',
            '>': 'v'
        },
        '<': {
            '^': '>^',
            'A': '>>^',
            'v': '>',
            '>': '>>'
        },
        'v': {
            '^': '^',
            'A': '^>',
            '<': '<',
            '>': '>'
        },
        '>': {
            '^': '<^',
            'A': '^',
            '<': '<<',
            'v': '<'
        }
    }

    f = open("inputs/day-21.txt", "r")

    complexities_sum = 0
    for line in f:
        line = line.strip()
        num = int(re.sub("\D", "", line))

        numeric_instructions = get_instructions(line, best_numeric_paths)
        # print("n", numeric_instructions)

        len = dfs(numeric_instructions, best_direction_paths, {}, 25)
        # print("d2", len)

        complexities_sum += num * len

    f.close()
    return complexities_sum

print(solve_day21_puzzle1())