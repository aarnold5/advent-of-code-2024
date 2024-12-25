def sort_func(e):
  return len(e)


def starts_with_pattern(s, patterns, prev_s_results):
    if s == '':
        return 1
    
    if s in prev_s_results:
        return prev_s_results[s]
    
    total_worked_count = 0
    for pattern in patterns:
        if s[0:len(pattern)] == pattern:
            worked_count = starts_with_pattern(s[len(pattern):], patterns, prev_s_results)
            prev_s_results[s[len(pattern):]] = worked_count
            total_worked_count += worked_count

    return total_worked_count


def solve_day19_puzzle2():
    f = open("inputs/day-19.txt", "r")

    second_half = False

    designs = []
    patterns = []
    
    for line in f:
        if line == '\n':
            second_half = True
        elif not second_half:
            whole_patterns = line.split(",")
            for pattern in whole_patterns:
                patterns.append(pattern.strip())
        
        else:
            designs.append(line.strip())
    f.close()

    patterns.sort(key=sort_func, reverse=True)

    combos = 0 
    prev_s_results = {}
    for design in designs:
        number_combos = starts_with_pattern(design, patterns, prev_s_results)
        combos += number_combos

    return combos

 
print(solve_day19_puzzle2())

