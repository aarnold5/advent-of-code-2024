import re

def solve_day3_puzzle2():
    f = open("inputs/day-3.txt", "r")
    text = f.read()

    result = 0
    
    dont_split = text.split("don't()")
    for i in range(len(dont_split)):
        if i == 0:
            result += find_mul_numbers(dont_split[i])
        else:
            do_split = dont_split[i].split("do()")
            for i in range(1, len(do_split)):
                result += find_mul_numbers(do_split[i])

    f.close()
    return result

def find_mul_numbers(text):
    result = 0
    valid_instructions = re.findall("mul\((\d*,\d*)\)",text)
    for instruction in valid_instructions:
        parts = instruction.split(",")
        result += int(parts[0]) * int(parts[1])
    return result

print(solve_day3_puzzle2())