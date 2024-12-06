def solve_day5_puzzle1():
    rules = {}
    sum = 0

    f = open("inputs/day-5.txt", "r")
    for line in f:
        if line == '\n':
            continue

        split = line.strip().split("|")
        if len(split) == 2:
            x = split[0]
            y = split[1]
            if x not in rules:
                rules[x] = []
            rules[x].append(y)

        else:
            seen_before = set()
            pages = line.strip().split(',')
            valid = True

            for num in pages:
                if num in rules:
                    nums_that_must_be_after = rules[num]
                    for n in nums_that_must_be_after:
                        if n in seen_before:
                            valid = False
                            break

                seen_before.add(num)

            if valid:
                sum += int(pages[len(pages)//2])

    f.close()
    return sum

print(solve_day5_puzzle1())