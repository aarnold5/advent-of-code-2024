# Had to look up an explaination of all this. I got the idea for this manual parsing helper code from someone else online
def solve_day24_puzzle2():
    f = open("inputs/day-24.txt", "r")

    to_do = {}

    second_half = False
    for line in f:
        if line == '\n':
            second_half = True
            continue
        if second_half:
            (wire1, gate, wire2, arrow, res_wire) = line.split()
            to_do[res_wire] = (wire1, gate, wire2)

    f.close()

    # print_tree('z45', 0, to_do)
    
    correct = True
    i = 0
    while correct and i < 45:
        z_wire = get_wire_name('z', i)
        res = verify_z_wire(z_wire, i, to_do)
        correct = res
        if not correct:
            print("failed for wire " + z_wire)
        i += 1


def print_tree(res_wire, depth, to_do):
    if res_wire[0] == 'x' or res_wire[0] == 'y':
        print("  " * depth + res_wire)
    else:
        (wire1, gate, wire2) = to_do[res_wire]
        print("  " * depth, gate, res_wire)
        print_tree(wire1, depth+1, to_do)
        print_tree(wire2, depth+1, to_do)


def get_wire_name(wire, num):
    return wire + str(num).rjust(2, '0')


def verify_z_wire(res_wire, num, to_do):
    print('zw', res_wire, num)
    (wire1, gate, wire2) = to_do[res_wire]
    if gate != 'XOR': 
        return False
    if num == 0:
        return (wire1 == 'x00' and wire2 == 'y00') or (wire1 == 'y00' and wire2 == 'x00')
    return (verify_intermediate_xor(wire1, num, to_do) and verify_carry(wire2, num, to_do)) or (verify_intermediate_xor(wire2, num, to_do) and verify_carry(wire1, num, to_do))
    

def verify_intermediate_xor(res_wire, num, to_do):
    print("ix", res_wire, num)
    (wire1, gate, wire2) = to_do[res_wire]
    if gate != 'XOR':
        return False
    return (wire1 == get_wire_name('x', num) and wire2 == get_wire_name('y', num)) or (wire1 == get_wire_name('y', num) and wire2 == get_wire_name('x', num))


def verify_carry(res_wire, num, to_do):
    print("cb", res_wire, num)
    (wire1, gate, wire2) = to_do[res_wire]
    if num == 1:
        if gate != 'AND':
            return False
        return ((wire1 == 'x00' and wire2 == 'y00') or (wire1 == 'y00' and wire2 == 'x00'))
    if gate != 'OR': 
        return False
    return (verify_direct_carry(wire1, num-1, to_do) and verify_recarry(wire2, num-1, to_do)) or (verify_direct_carry(wire2, num-1, to_do) and verify_recarry(wire1, num-1, to_do))


def verify_direct_carry(res_wire, num, to_do):
    print("dc", res_wire, num)
    (wire1, gate, wire2) = to_do[res_wire]
    if gate != 'AND':
        return False
    return (wire1 == get_wire_name('x', num) and wire2 == get_wire_name('y', num)) or (wire1 == get_wire_name('y', num) and wire2 == get_wire_name('x', num))


def verify_recarry(res_wire, num, to_do):
    print("rc", res_wire, num)
    (wire1, gate, wire2) = to_do[res_wire]
    if gate != 'AND':
        return False
    return (verify_intermediate_xor(wire1, num, to_do) and verify_carry(wire2, num, to_do)) or (verify_intermediate_xor(wire2, num, to_do) and verify_carry(wire1, num, to_do))


print(solve_day24_puzzle2())