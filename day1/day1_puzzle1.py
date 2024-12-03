from day1_shared import getLists


def solve_day1_puzzle1():
    lists = getLists()
    l1 = lists[0]
    l2 = lists[1]

    l1.sort()
    l2.sort()

    total_dif = 0
    for i in range(len(l1)):
        total_dif += abs(l1[i] - l2[i])

    return total_dif

print(solve_day1_puzzle1())