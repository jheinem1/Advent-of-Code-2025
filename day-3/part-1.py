import re

def add_results(section):
    mul_instructions = parse_mul_instructions(section)

    results = 0
    for x, y in mul_instructions:
        results += x * y
    return results

def parse_mul_instructions(section):
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(mul_pattern, section)

    mul_instructions = []
    for match in matches:
        x, y = match
        mul_instructions.append([int(x), int(y)])
    return mul_instructions

with open('day-3/input.txt', 'r') as f:
    input_data = f.read().strip()
    
added_results = add_results(input_data)
print(added_results)