import itertools


def solve_day7_puzzle2():
    f = open("inputs/day-7.txt", "r")

    total_calibration_result = 0

    for line in f:
        # Get the strings as integer values
        [test_value_string, operands_string] = line.split(":")
        operands_string_array = operands_string.split()

        test_value = int(test_value_string)
        operands = []
        for s in operands_string_array:
            operands.append(int(s))

        print("testing line: " + line.strip())
        # Get all the posible combos and test them
        possible_operator_combos = list(itertools.product(['+', '*', '||'], repeat=len(operands)-1))
        for combo in possible_operator_combos:
            res = operands[0]
            for i in range(1, len(operands)):
                operator = combo[i-1]
                operand = operands[i]
                if operator == '+':
                    res += operand
                elif operator == '*':
                    res *= operand
                elif operator == '||':
                    s = str(res) + str(operand)
                    res = int(s)

            if res == test_value:
                total_calibration_result += test_value
                break

    f.close()
    return total_calibration_result


print(solve_day7_puzzle2())