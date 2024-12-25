def sort_func(e):
  return len(e)


def starts_with_pattern(s, patterns, prev_s_results):
    if s == '':
        return True
    
    if s in prev_s_results:
        return prev_s_results[s]
    
    for pattern in patterns:
        if s[0:len(pattern)] == pattern:
            worked = starts_with_pattern(s[len(pattern):], patterns, prev_s_results)
            prev_s_results[s[len(pattern):]] = worked
            if worked:
                return True
            else:
                continue

        
    return False


def solve_day19_puzzle1():
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

    valid_count = 0 
    prev_s_results = {}
    for design in designs:
        design_possible = starts_with_pattern(design, patterns, prev_s_results)
        if design_possible:
            valid_count += 1

    return valid_count

 
print(solve_day19_puzzle1())

