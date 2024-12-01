with open('day-1/input.txt', 'r') as f:
    input = f.read()

    left_list = []
    right_list = []
    for line in input.splitlines():
        columns = line.split('   ')
        left_list.append(int(columns[0]))
        right_list.append(int(columns[1]))
    
    # pair up smallest number in left list with smallest number in right list and so on
    # implemented by sorting each list since they're the same length
    left_list.sort()
    right_list.sort()
    
    # find distance between the pairs and add them up
    total_distance_between_pairs = 0
    for i in range(len(left_list)):
        total_distance_between_pairs += abs(left_list[i] - right_list[i])

    # output total distance between pairs
    print(total_distance_between_pairs)