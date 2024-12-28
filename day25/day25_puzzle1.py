from enum import Enum

class ItemType(Enum):
    LOCK = 'LOCK'
    KEY = 'KEY'

def solve_day25_puzzle1():
    f = open("inputs/day-25.txt", "r")

    locks = []
    keys = []
    curr_item = None
    curr_item_type = ItemType.LOCK

    line_of_item = 0

    for line in f:
        line = line.strip()
        # The end of the curr_item was reached. Save the curr_item
        if line == '':
            if (curr_item_type == ItemType.LOCK):
                locks.append(curr_item)
            elif (curr_item_type == ItemType.KEY):
                keys.append(curr_item)
            curr_item = None
            line_of_item = 0
        # First line of a lock
        elif curr_item == None and line == "#####":
            curr_item_type = ItemType.LOCK
            curr_item = [0,0,0,0,0]
            line_of_item = 0
        # First line of a key
        elif curr_item == None and line == ".....":
            curr_item_type = ItemType.KEY
            curr_item = [0,0,0,0,0]
            line_of_item = 0
        # Works on making the height map for the current item
        else:
            if curr_item_type == ItemType.KEY and line_of_item == 5:
                continue
            for i in range(len(line)):
                if line[i] == '#':
                    curr_item[i] += 1
            line_of_item += 1
    
    # Add the last item
    if (curr_item_type == ItemType.LOCK):
        locks.append(curr_item)
    elif (curr_item_type == ItemType.KEY):
        keys.append(curr_item)

    f.close()

    count_pairs = 0
    for lock in locks:
        for key in keys:
            all_fit = True
            for i in range(len(lock)):
                if lock[i] + key[i] >= 6:
                    all_fit = False
                    break
            if all_fit:
                count_pairs += 1

    return count_pairs

print(solve_day25_puzzle1())