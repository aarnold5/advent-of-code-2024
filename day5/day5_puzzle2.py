def solve_day5_puzzle2():
    rules = {}
    sum = 0

    f = open("inputs/day-5.txt", "r")
    for line in f:
        if line == '\n':
            continue

        split = line.strip().split("|")
        if len(split) == 2:
            x = split[0]
            y = split[1]
            if x not in rules:
                rules[x] = []
            rules[x].append(y)

        else:
            pages = line.strip().split(',')

            valid = test_validity(rules, pages)

            if not valid:
                newPages = rearrange(rules, pages)
                sum += int(newPages[len(newPages)//2])

    f.close()
    return sum

def test_validity(rules, pages):
    seen_before = set()
    valid = True

    for num in pages:
        if num in rules:
            nums_that_must_be_after = rules[num]
            for n in nums_that_must_be_after:
                if n in seen_before:
                    valid = False
                    break

        seen_before.add(num)

    return valid

def rearrange(rules, pages):
    new_list = []
    seen_before = set()

    for num in pages:
        num_was_added = False 
        if num in rules:
            nums_that_must_be_after = rules[num]
            for n in nums_that_must_be_after:
                if n in seen_before:
                    new_list.insert(new_list.index(n), num)
                    num_was_added = True
                    break
            
        if not num_was_added:
            new_list.append(num)
                    
        seen_before.add(num)

    if test_validity(rules, new_list):
        return new_list
    else:
        return rearrange(rules, new_list)

print(solve_day5_puzzle2())