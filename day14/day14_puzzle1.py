import re


def solve_day14_puzzle1(width, height, input):
    f = open(input, "r")
    
    robotInfo = []

    for line in f:
        pieces = [int(s) for s in re.findall(r'(-?[\d]+)', line)]
        robotInfo.append(pieces)

    f.close()

    for i in range(len(robotInfo)):
        robot = robotInfo[i]
        for j in range(100):
            (new_px, new_py) = move(robot[0], robot[1], robot[2], robot[3], width, height)
            robot[0] = new_px
            robot[1] = new_py

    mid_x = width//2
    mid_y = height//2

    total_q1 = 0
    total_q2 = 0
    total_q3 = 0
    total_q4 = 0

    for robot in robotInfo:
        [x, y, vx, vy] = robot
        if x > mid_x and y < mid_y:
            total_q1 += 1
        elif x < mid_x and y < mid_y:
            total_q2 += 1
        elif x < mid_x and y > mid_y:
            total_q3 += 1
        elif x > mid_x and y > mid_y:
            total_q4 += 1

    return total_q1 * total_q2 * total_q3 * total_q4


def move(px, py, vx, vy, width, height):
    new_px = px + vx
    new_py = py + vy

    if new_px > width-1:
        new_px = new_px-width
    if new_px < 0:
        new_px = width+new_px
    if new_py > height-1:
        new_py = new_py-height
    if new_py < 0:
        new_py = height+new_py

    return (new_px, new_py)


# print(solve_day14_puzzle1(11, 7, "inputs/test-day-14.txt"))
print(solve_day14_puzzle1(101, 103, "inputs/day-14.txt"))


    