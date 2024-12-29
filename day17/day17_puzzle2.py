def get_output(register_a, register_b, register_c, program):
    pointer = 0

    output = []

    while pointer + 1 < len(program):
        opcode = program[pointer]
        operand = program[pointer+1]
        combo_operand = get_combo_operand(operand, register_a, register_b, register_c)

        if opcode == 0:
            register_a = register_a // 2 ** combo_operand

        elif opcode == 1:
            register_b = register_b ^ operand

        elif opcode == 2:
            register_b = combo_operand % 8

        elif opcode == 3:
            if register_a != 0:
                pointer = operand
                continue

        elif opcode == 4:
            register_b = register_b ^ register_c

        elif opcode == 5:
            output.append(str(combo_operand % 8))

        elif opcode == 6:
            register_b = register_a // 2 ** combo_operand

        elif opcode == 7:
            register_c = register_a // 2 ** combo_operand

        pointer += 2

    return (",".join(output))


def get_combo_operand(operand, register_a, register_b, register_c):
    if operand == 0 or operand == 1 or operand == 2 or operand == 3:
        return operand
    elif operand == 4:
        return register_a
    elif operand == 5:
        return register_b
    elif operand == 6:
        return register_c


def solve_day17_puzzle2():
    f = open("inputs/day-17.txt", "r")
    
    register_a = 0
    register_b = 0
    register_c = 0

    program = []
    output_string = ''

    for line in f:
        if line != '\n':
            line = line.split(":")
            if line[0].endswith("A"):
                register_a = int(line[1].strip())
            elif line[0].endswith("B"):
                register_b = int(line[1].strip())
            elif line[0].endswith("C"):
                register_c = int(line[1].strip())
            elif line[0].endswith("Program"):
                output_string = line[1].strip()
                program_string = output_string.split(',')
                for num in program_string:
                    program.append(int(num))
    f.close()

    # The first value of a that gives len_program output values would be 8**(len_program-1). This is because the program stops outputting when a == 0 and a is reset every iteration to itself divided by 8 rounded down to the nearest integer
    # The last a value that would give len_program output values would be 8**len_program
    len_program = len(program)
    return get_a_value(8**(len_program-1), 8**len_program, 8**(len_program-1), output_string, 1, register_b, register_c, program, None)


def get_a_value(start, end, incr_interval, target_output, depth, register_b, register_c, program, min_val):
    intervals_to_check = []
    for a in range(start, end, incr_interval):
        out = get_output(a, register_b, register_c, program)
        if out.endswith(target_output[len(target_output)-depth:]):
            intervals_to_check.append((a, a+incr_interval))
            if depth == len(target_output):
                return a
            
    if len(intervals_to_check) == 0:
        return

    for interval in intervals_to_check:
        val = get_a_value(interval[0], interval[1], incr_interval // 8, target_output, depth + 2, register_b, register_c, program, min_val)
        if val != None and min_val == None:
            min_val = val
        elif val != None and min_val != None:
            min_val = min(val, min_val)

    return min_val     


print(solve_day17_puzzle2())