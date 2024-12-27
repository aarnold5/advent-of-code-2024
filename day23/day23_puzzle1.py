def solve_day23_puzzle1():
    f = open("inputs/day-23.txt", "r")

    connections = {}
    sets = set()
    for line in f:
        computers = line.strip().split("-")
        if computers[0] not in connections:
            connections[computers[0]] = set()
        if computers[1] not in connections:
            connections[computers[1]] = set()
        connections[computers[0]].add(computers[1])
        connections[computers[1]].add(computers[0])

    f.close()

    num_contain_t = 0
    for comp0 in connections:
        for comp1 in connections[comp0]:
            shared = connections[comp0].intersection(connections[comp1])
            for item in shared:
                all_items = sorted([item, comp0, comp1])
                alpha_tuple = (all_items[0], all_items[1], all_items[2])
                if alpha_tuple not in sets:
                    sets.add(alpha_tuple)
                    if (item[0] == 't' or comp0[0] == 't' or comp1[0] == 't'):
                        num_contain_t += 1

    return num_contain_t

print(solve_day23_puzzle1())