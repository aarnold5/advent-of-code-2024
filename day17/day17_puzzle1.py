def solve_day17_puzzle1():
    f = open("inputs/day-17.txt", "r")
    
    register_a = 0
    register_b = 0
    register_c = 0

    program = []

    pointer = 0

    output = []

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
                program_string = line[1].strip().split(',')
                for num in program_string:
                    program.append(int(num))
    f.close()

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


print(solve_day17_puzzle1())