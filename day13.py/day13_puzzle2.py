import re

def solve_day13_puzzle2():
    f = open("inputs/day-13.txt", "r")
    
    machine_info = [[]]
    machine_idx = 0

    # Get the machine info from the text
    for line in f:
        if line == '\n':
            machine_idx += 1
            machine_info.append([])
        else:
            pieces = [int(s) for s in re.findall(r'\b\d+\b', line)]
            machine_info[machine_idx].append(pieces)

    f.close()

    total_tokens = 0
    for machine in machine_info:
        [A, B, P] = machine
        P[0] = P[0] + 10000000000000
        P[1] = P[1] + 10000000000000

        [AX, BX, PX] = [A[0]*A[1], B[0]*A[1], P[0]*A[1]]
        [AY, BY, PY] = [A[1]*A[0], B[1]*A[0], P[1]*A[0]]
        b = (PX - PY) / (BX - BY)
        a = (P[0] - B[0] * b) / A[0]

        are_int = a.is_integer() and b.is_integer()
        if are_int:
            total_tokens += int(a)*3+int(b)*1
                    
    return total_tokens

print(solve_day13_puzzle2())
    