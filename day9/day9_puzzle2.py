def solve_day9_puzzle2():
    f = open("inputs/day-9.txt", "r")
    text = f.read().strip()

    id = 0
    blocks = []
    blocks_idx = -1

    file_block = []
    empty_block = []


    # Create the blocks and keep track of where the start and end of each are
    for i in range(len(text)):
        num = int(text[i])

        if i % 2 == 0:
            start = blocks_idx + 1
            for j in range(num):
                blocks.append(id)
                blocks_idx += 1
            end = blocks_idx
            file_block.append((start, end, num))
            id += 1
                
        else:
            start = blocks_idx + 1
            for j in range(num):
                blocks.append('.')
                blocks_idx += 1
            end = blocks_idx
            empty_block.append((start, end, num))

    f.close()
    
    # Compact the hard drive
    for i in range(len(file_block)-1, -1, -1):
        empty_block_idx = 0
        (file_start, file_end, num_in_block) = file_block[i]
        num = blocks[file_start]

        print("attempting to move id " + str(num))

        while empty_block[empty_block_idx][1] < file_start:
            (empty_start, empty_end, num_empty) = empty_block[empty_block_idx]
            if (num_empty >= num_in_block):
                for i in range(empty_start, empty_start + num_in_block):
                    blocks[i] = num
                for i in range(file_start, file_end + 1):
                    blocks[i] = '.'

                new_start = empty_start + num_in_block
                new_num_in_block = num_empty - num_in_block
                empty_block[empty_block_idx] = (new_start, empty_end, new_num_in_block)
                break
            else:
                empty_block_idx += 1

    checksum = 0
    for i in range(len(blocks)):
        if (blocks[i] != '.'):
            checksum += i * int(blocks[i])

    return checksum


print(solve_day9_puzzle2())