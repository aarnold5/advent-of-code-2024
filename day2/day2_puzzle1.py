def solve_day2_puzzle1():
    f = open("inputs/day-2.txt", "r")

    safe_count = 0
    prev_diff = 0

    for report in f:
        levels = report.split()
        safe = True

        for i in range(1, len(levels)):
            diff = int(levels[i]) - int(levels[i-1])
            abs_diff = abs(diff)
            
            diff_in_range = abs_diff <= 3 and abs_diff >= 1
            diff_sign_same = (diff > 0 and prev_diff > 0) or (diff < 0 and prev_diff < 0)

            if (i == 1 and diff_in_range) or (i > 1 and diff_sign_same and diff_in_range):
                prev_diff = diff
                continue
            else:
                safe = False
                break
        
        if safe:
            safe_count += 1

    f.close()

    return safe_count

print(solve_day2_puzzle1())