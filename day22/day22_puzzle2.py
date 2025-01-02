import sys


def mix(given_value, secret_number):
    secret_number = given_value ^ secret_number
    return secret_number

def prune(secret_number):
    secret_number = secret_number % 16777216
    return secret_number

def generate_prices(secret_num, depth, max_depth, prices_list):
    prices_list.append(secret_num % 10)

    if depth == max_depth:
        return
    
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

        return generate_prices(secret_num, depth+1, max_depth, prices_list)

def get_possible_sequences(prices, price_diffs):
    all_sequences = set()
    sequences_for_buyers = []
    for i in range(len(price_diffs)):
        sequences_for_buyers.append({})
        buyer = price_diffs[i]
        for j in range(3, len(buyer)):
            sequence = (buyer[j-3], buyer[j-2], buyer[j-1], buyer[j])
            if sequence not in sequences_for_buyers[i]:
                sequences_for_buyers[i][sequence] = prices[i][j+1]
            all_sequences.add(sequence)

    return (all_sequences, sequences_for_buyers)

def get_price_diffs(prices):
    price_diffs = []
    for i in range(len(prices)):
        buyer = prices[i]
        price_diffs.append([])
        for j in range(1,len(buyer)):
            prev_price = buyer[j-1]
            price = buyer[j]
            price_diffs[i].append(price - prev_price)

    return price_diffs

def solve_day22_puzzle2():
    sys.setrecursionlimit(3000) 
    f = open("inputs/day-22.txt", "r")

    prices = []
    line_idx = 0

    print('generating prices...')
    for line in f:
        initial_num = int(line.strip())
        prices.append([])
        generate_prices(initial_num, 0, 2000,  prices[line_idx])
        line_idx += 1

    f.close()
    
    print('getting price differences...')
    price_differences = get_price_diffs(prices)

    print('getting possible sequences...')
    (all_sequences, sequences_for_buyers) = get_possible_sequences(prices,price_differences)

    print('getting end banana amount for all sequences...')
    price_map = {}
    for sequence in all_sequences:
        price_map[sequence] = 0
        for buyer_map in sequences_for_buyers:
            if sequence in buyer_map:
                price_map[sequence] += buyer_map[sequence]

    print('finding max bananas...')
    max_bananas = 0
    max_sequence = None
    for sequence in price_map:
        price = price_map[sequence]
        if price > max_bananas:
            max_bananas = price
            max_sequence = sequence

    return max_sequence, max_bananas


print(solve_day22_puzzle2())