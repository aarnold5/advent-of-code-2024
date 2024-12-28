def solve_day24_puzzle1():
    f = open("inputs/day-24.txt", "r")

    have_seen = {}
    to_do = []
    z_wires = {}
    z_wires_complete = 0

    second_half = False
    for line in f:
        if line == '\n':
            second_half = True
            continue
        if not second_half:
            (wire, val) = line.split(':')
            have_seen[wire] = int(val.strip())
        else:
            (wire1, gate, wire2, arrow, res_wire) = line.split()
            to_do.append((wire1, gate, wire2, res_wire))
            if res_wire[0] == 'z':
                z_wires[res_wire] = None

    f.close()

    while z_wires_complete != len(z_wires):
        for i in range(len(to_do)):
            (wire1, gate, wire2, res_wire) = to_do[i]
            if wire1 in have_seen and wire2 in have_seen:
                res = None
                if gate == 'OR':
                    res = have_seen[wire1] or have_seen[wire2]
                elif gate == 'AND':
                    res = have_seen[wire1] and have_seen[wire2]
                else:
                    res = have_seen[wire1] ^ have_seen[wire2]
                have_seen[res_wire] = res

                if res_wire in z_wires:
                    z_wires[res_wire] = res
                    z_wires_complete += 1

                to_do.pop(i)
                break

    z_wires_sorted = sorted(z_wires.keys(), reverse=True)
    binary = ''
    for z in z_wires_sorted:
        binary +=  str(z_wires[z])

    return int(binary, 2)

print(solve_day24_puzzle1())