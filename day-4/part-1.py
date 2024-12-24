import numpy as np
import re

search_patterns = [r'XMAS', r'SAMX']

def find_matches(table) -> int:
    return find_num_horizontal_matches(table) + find_num_vertical_matches(table) + find_num_diagonal_matches(table)

def find_num_horizontal_matches(table) -> int:
    # concatenate each row into an array of strings
    rows = [''.join(row) for row in table]

    # find sum of number of matches in each row
    return sum([num_matches(row) for row in rows])

def find_num_vertical_matches(table) -> int:
    # concatenate each column into an array of strings
    columns = [''.join(column) for column in np.transpose(table)]

    # find sum of number of matches in each column
    return sum([num_matches(column) for column in columns])

def find_num_diagonal_matches(table) -> int:
    # concatenate each main diagonal into an array of strings
    main_diagonals = [
        ''.join(np.diagonal(table, i))
        for i in range(-table.shape[0] + 1, table.shape[1])
    ]

    # concatenate each anti-diagonal into an array of strings
    flipped_table = np.fliplr(table)
    anti_diagonals = [
        ''.join(np.diagonal(flipped_table, i))
        for i in range(-flipped_table.shape[0] + 1, flipped_table.shape[1])
    ]

    return sum(num_matches(d) for d in main_diagonals) \
         + sum(num_matches(d) for d in anti_diagonals)

def num_matches(string) -> int:
    return sum([len(re.findall(pattern, string)) for pattern in search_patterns])

with open('day-4/input.txt', 'r') as f:
    input_data = f.read().strip()

table = np.array([list(row) for row in input_data.split('\n')])
matches = find_matches(table)
print(matches)
