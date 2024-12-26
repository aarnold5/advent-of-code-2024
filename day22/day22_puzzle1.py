import sys


def mix(given_value, secret_number):
    secret_number = given_value ^ secret_number
    return secret_number

def prune(secret_number):
    secret_number = secret_number % 16777216
    return secret_number

def generate_secret_number(secret_num, depth, max_depth):
    if depth == max_depth:
        return secret_num
    
    else:
        res = secret_num * 64
        secret_num = mix(res, secret_num)
        secret_num = prune(secret_num)

        res = secret_num // 32
        secret_num = mix(res, secret_num)
        secret_num = prune(secret_num)

        res = secret_num * 2048
        secret_num = mix(res, secret_num)
        secret_num = prune(secret_num)

        return generate_secret_number(secret_num, depth+1, max_depth)
        

def solve_day22_puzzle1():
    sys.setrecursionlimit(3000) 
    f = open("inputs/day-22.txt", "r")

    res_sum = 0
    for line in f:
        initial_num = int(line.strip())
        secret_num = generate_secret_number(initial_num, 0, 2000)
        res_sum += secret_num

    f.close()
    return res_sum

print(solve_day22_puzzle1())