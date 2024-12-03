import re

def solve_day3_puzzle1():
    f = open("inputs/day-3.txt", "r")
    text = f.read()

    result = 0
    
    valid_instructions = re.findall("mul\((\d*,\d*)\)",text)
    for instruction in valid_instructions:
        parts = instruction.split(",")
        result += int(parts[0]) * int(parts[1])

    f.close()
    return result

print(solve_day3_puzzle1())