import numpy as np

def find_matches(table) -> int:
    matches = 0
    for x in range(len(table) - 2):
        for y in range(len(table[x]) - 2):
            matches += 1 if is_valid_square(table[x:x + 3, y:y + 3]) else 0

    return matches

def is_valid_square(square) -> bool:
    if square[1][1] == 'A':
        main_diagonal = ''.join(np.diagonal(square))
        main_diagonal_valid = False
        if main_diagonal == 'MAS' or main_diagonal == 'SAM':
            main_diagonal_valid = True
        anti_diagonal = ''.join(np.diagonal(np.fliplr(square)))
        anti_diagonal_valid = False
        if anti_diagonal == 'MAS' or anti_diagonal == 'SAM':
            anti_diagonal_valid = True
        
        return main_diagonal_valid and anti_diagonal_valid

    return False

with open('day-4/input.txt', 'r') as f:
    input_data = f.read().strip()

table = np.array([list(row) for row in input_data.split('\n')])
matches = find_matches(table)
print(matches)
