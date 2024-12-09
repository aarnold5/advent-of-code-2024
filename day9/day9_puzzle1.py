def solve_day9_puzzle1():
    f = open("inputs/day-9.txt", "r")
    text = f.read().strip()

    id = 0
    blocks = []

    for i in range(len(text)):
        num = int(text[i])
        if i % 2 == 0:
            for j in range(num):
                blocks.append(id)
            id += 1
                
        else:
            for j in range(num):
                blocks += '.'
    f.close()

    no_gaps = []
    for c in blocks:
        if c == '.':
            while len(blocks) > 0 and blocks[-1] == '.':
                blocks.pop()
            no_gaps.append(blocks.pop())
        else:
            no_gaps.append(c)

    checksum = 0
    for i in range(len(no_gaps)):
        checksum += i * no_gaps[i]

    return checksum


print(solve_day9_puzzle1())