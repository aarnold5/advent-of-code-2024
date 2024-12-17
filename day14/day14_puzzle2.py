import re


def solve_day14_puzzle1(width, height, input):
    f = open(input, "r")
    
    robotInfo = []

    for line in f:
        pieces = [int(s) for s in re.findall(r'(-?[\d]+)', line)]
        robotInfo.append(pieces)

    f.close()

    mid_x = width//2
    mid_y = height//2
    safetys = {}
    f_write = open('scores.txt', "w")
    for j in range(10000):
        total_q1 = 0
        total_q2 = 0
        total_q3 = 0
        total_q4 = 0

        for i in range(len(robotInfo)):
            robot = robotInfo[i]
            (new_px, new_py) = move(robot[0], robot[1], robot[2], robot[3], width, height)
            robot[0] = new_px
            robot[1] = new_py

            if new_px > mid_x and new_py < mid_y:
                total_q1 += 1
            elif new_px < mid_x and new_py < mid_y:
                total_q2 += 1
            elif new_px < mid_x and new_py > mid_y:
                total_q3 += 1
            elif new_px > mid_x and new_py > mid_y:
                total_q4 += 1

        safety_score = total_q1 * total_q2 * total_q3 * total_q4
        safetys[safety_score] = j+1 # plus 1 to account for how indexes work

        f_write.write(str(safety_score) + ", " + str(j+1) + "\n")

        # draw if the score is lower than a certain amount
        # the images look closer to what we are looking for when the score is lower
        if len(str(safety_score)) <= 8:
            new_map = draw_positions(width, height, robotInfo, (mid_x, mid_y))

            with open('files/file' + str(j+1) + '.txt', 'w') as f_write2:
                for line in new_map:
                    f_write2.write(str(line) + '\n')

    f_write.close()
    print(safetys[min(safetys)])

    return


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


def draw_positions(width, height, robotInfo, midpoint):
    robotMap = []
    for y in range(height):
        robotMap.append([])
        for x in range(width):
            count = 0
            for z in range(len(robotInfo)):
                if x == robotInfo[z][0] and y == robotInfo[z][1]:
                    count += 1
 
            if count == 0:
                robotMap[y].append('.')
            else:
                robotMap[y].append(str(count))

    return robotMap


#print(solve_day14_puzzle1(11, 7, "inputs/test-day-14.txt"))
print(solve_day14_puzzle1(101, 103, "inputs/day-14.txt"))


    