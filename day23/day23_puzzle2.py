def check_connections(current_group, current_group_neighbors, potential_members, connections_map, curr_max_group):
    print(current_group, current_group_neighbors, potential_members, curr_max_group)
    print('\n')
    if len(potential_members) == 0:
        if len(current_group) <= len(curr_max_group):
            current_group.pop()
            current_group_neighbors.pop()
            return curr_max_group
        
        all_match = True
        for i in range(len(current_group_neighbors)):
            for j in range(len(current_group)):
                if i != j:
                    if current_group[j] not in current_group_neighbors[i]:
                        all_match = False
            
        if all_match:
            curr_max_group = set(current_group)

        current_group.pop()
        current_group_neighbors.pop()
        return curr_max_group
    
    for member in potential_members:
        if member not in current_group:
            # print(current_group_neighbors, connections_map[member])
            shared = set.intersection(*current_group_neighbors).intersection(connections_map[member])
            current_group.append(member)
            current_group_neighbors.append(connections_map[member])
            curr_max_group = check_connections(current_group, current_group_neighbors, shared, connections_map, curr_max_group)

    if len(current_group) > len(curr_max_group):
        curr_max_group = set(current_group)
    return curr_max_group
            

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

    max_group = None
    for c in connections:
        current_group = [c]
        current_group_neighbors = [connections[c]]
        potential_members = connections[c]
        if not max_group:
            max_group = set(current_group)
        this_max = check_connections(current_group, current_group_neighbors, potential_members, connections, max_group)
        print("This Group", current_group, this_max)
        if len(this_max) > len(max_group):
            max_group = this_max

    alpha_max_sort = sorted(list(max_group))
    return ','.join(alpha_max_sort)

print(solve_day23_puzzle1())