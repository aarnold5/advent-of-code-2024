def getLists():
    l1 = []
    l2 = []

    f = open("inputs/day-1-puzzle-1.txt", "r")
    for line in f:
        row = line.split()
        l1.append(int(row[0]))
        l2.append(int(row[1]))

    f.close()

    return [l1, l2]
