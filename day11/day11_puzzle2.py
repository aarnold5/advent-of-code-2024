def solve_day11_puzzle2():
    f = open("inputs/day-11.txt", "r")
    
    stones = f.read().split()
    f.close()

    seen_map = {}
    stone_count = 0
    for stone in stones:
        stone_count += dfs(int(stone), seen_map, 0, 75)

    return stone_count


def get_neighbors(num, depth):
    neighbors = []

    str_num = str(num)
    len_str_num = len(str_num)
    new_depth = depth + 1

    if num == 0:
        neighbors.append((1, new_depth))
    elif len_str_num % 2 == 0:
        right_half_start = len_str_num // 2

        left_half = str_num[:right_half_start]
        right_half = str_num[right_half_start:]

        neighbors.append((int(right_half), new_depth))
        neighbors.append((int(left_half), new_depth))
    else:
        neighbors.append((num * 2024, new_depth))

    return neighbors


def dfs(num, seen_map, depth, max_depth):
    if (depth == max_depth):
        return 1
    
    neighbors = get_neighbors(num, depth)
    neighbor_sum = 0
    for n in neighbors:
        if n not in seen_map:
            neighbor_sum += dfs(n[0], seen_map, n[1], max_depth)
        else:
            neighbor_sum += seen_map[n]
    
    seen_map[(num, depth)] = neighbor_sum
    return seen_map[(num, depth)]


print(solve_day11_puzzle2())