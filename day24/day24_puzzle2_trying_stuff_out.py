def solve_day24_puzzle2():
    f = open("inputs/day-24.txt", "r")

    have_seen = {}
    to_do = []
    z_wires = {}
    z_wires_complete = 0

    x_wires = {}
    y_wires = {}
    z_to_dos = []

    second_half = False
    for line in f:
        if line == '\n':
            second_half = True
            continue
        if not second_half:
            (wire, val) = line.split(':')
            have_seen[wire] = int(val.strip())
            if wire[0] == 'x':
                x_wires[wire] = int(val.strip())
            elif wire[0] == 'y':
                y_wires[wire] = int(val.strip())
        else:
            (wire1, gate, wire2, arrow, res_wire) = line.split()
            to_do.append((wire1, gate, wire2, res_wire))
            if res_wire[0] == 'z':
                z_to_dos.append((wire1, gate, wire2, res_wire))
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
                
                print(to_do[i], res)
                to_do.pop(i)
                break

    z_wires_sorted = sorted(z_wires.keys(), reverse=True)
    z_binary = ''
    for z in z_wires_sorted:
        z_binary +=  str(z_wires[z])

    x_wires_sorted = sorted(x_wires.keys(), reverse=True)
    x_binary = ''
    for x in x_wires_sorted:
        x_binary +=  str(x_wires[x])

    y_wires_sorted = sorted(y_wires.keys(), reverse=True)
    y_binary = ''
    for y in y_wires_sorted:
        y_binary +=  str(y_wires[y])

    x = int(x_binary, 2)
    y = int(y_binary, 2)
    z = int(z_binary, 2)

    expected_z = x + y
    expected_z_binary = bin(expected_z)[2:]

    incorrect_bit_idxs = {}
    for i in range(len(z_binary)-1, -1, -1):
        if z_binary[i] != expected_z_binary[i]:
            incorrect_bit_idxs[len(z_binary)-1-i] = expected_z_binary[i]
        
    print('\n')
    for i in range(len(z_to_dos)):
        if i in incorrect_bit_idxs:
            print(z_to_dos[i])
    
    # print(have_seen)
    print(z_binary)
    print(expected_z_binary)
    print(incorrect_bit_idxs)

    return int(z_binary, 2)

print(solve_day24_puzzle2())