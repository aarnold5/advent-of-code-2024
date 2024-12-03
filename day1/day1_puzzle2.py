from day1_shared import getLists


def solve_day1_puzzle2():
    lists = getLists()
    left = lists[0]
    right = lists[1]
    
    right_counts = {}
    for num in right:
        if num in right_counts:
            right_counts[num] += 1
        else:
            right_counts[num] = 1

    similarity = 0
    for num in left:
        if num in right_counts:
            incr = num * right_counts[num]
            similarity += incr

    return similarity

print(solve_day1_puzzle2())