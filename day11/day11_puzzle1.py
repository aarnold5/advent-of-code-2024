def solve_day11_puzzle1():
    f = open("inputs/day-11.txt", "r")
    
    stones = f.read().split()
    f.close()

    for i in range(25):
        j = 0
        while j < len(stones):
            str_stone = str(stones[j])
            int_stone = int(stones[j])

            if int_stone == 0:
                stones[j] = 1
            elif len(str_stone) % 2 == 0:
                right_half_start = len(str_stone) // 2

                left_half = str_stone[:right_half_start]
                right_half = str_stone[right_half_start:]

                stones.insert(j, int(left_half))
                j += 1

                stones[j] = int(right_half)
            else:
                stones[j] = int_stone * 2024

            j += 1

    return len(stones)


print(solve_day11_puzzle1())