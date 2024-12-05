import re

def add_results(section):
    instructions = parse_instructions(section)

    results = 0
    do = True
    for instruction in instructions:
        if instruction['type'] == 'do':
            do = True
        elif instruction["type"] == "don't":
            do = False
        elif instruction["type"] == 'mul' and do:
            results += instruction['arg1'] * instruction['arg2']
    return results

def parse_instructions(section):
    instruction_pattern = r"([a-zA-Z']+)\((\d{1,3})?,?(\d{1,3})?\)"
    matches = re.findall(instruction_pattern, section)

    instructions = []
    for match in matches:
        instruction, arg1, arg2 = match
        instruction = instruction.lower()
        if instruction.endswith("don't"):
            instructions.append({'type': "don't"})
        elif instruction.endswith('do'):
            instructions.append({'type': 'do'})
        elif instruction.endswith('mul') and arg1 and arg2:
            instructions.append({'type': 'mul', 'arg1': int(arg1), 'arg2': int(arg2)})
    return instructions

with open('day-3/input.txt', 'r') as f:
    input_data = f.read().strip()
    
added_results = add_results(input_data)
print(added_results)
