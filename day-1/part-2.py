with open('day-1/input.txt', 'r') as f:
    input = f.read()

    left_list = []
    right_list = []
    for line in input.splitlines():
        columns = line.split('   ')
        left_list.append(int(columns[0]))
        right_list.append(int(columns[1]))
    
    # multiply each number in left list by number of occurrences in right list
    for i in range(len(left_list)):
        left_list[i] = left_list[i] * right_list.count(left_list[i])

    # add up items in left list
    left_list_total = sum(left_list)

    # output similarity score
    print(left_list_total)