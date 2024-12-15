import re

def solve_day13_puzzle1():
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
        win_possible = False
        min_price = None
        [A, B, P] = machine
        for num_a in range(100):
            for num_b in range(100):
                if ((num_a)*(A[0]) + (num_b)*(B[0]) == P[0]) and ((num_a)*(A[1]) + (num_b)*(B[1]) == P[1]):
                    win_possible = True
                    price = num_a*3 + num_b*1
                    if min_price is None:
                        min_price = price
                    else:
                        min_price = min(price)

        if win_possible and min_price != None:
            total_tokens += min_price
                    
    return total_tokens

print(solve_day13_puzzle1())
    