# this will check if the report is safe on its own or 
# if it can be made safe by removing a single bad level
def is_safe(report):
    levels = [int(level) for level in report.split()]
    
    # check if report is safe without removing any levels
    if check_sequence(levels):
        return True
    
    # try removing each level one-by-one to determine if 
    # the sequence is safe
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if check_sequence(new_levels):
            return True
        
    return False

def check_sequence(levels):
    # a single level is always safe
    if len(levels) < 2:
        return True
    
    # check whether sequence is gradually increasing
    increasing = all(levels[i] < levels[i+1] and 1 <= levels[i+1] - levels[i] <= 3 for i in range(len(levels)-1))
    
    # check whether sequence is gradually decreasing
    decreasing = all(levels[i] > levels[i+1] and 1 <= levels[i] - levels[i+1] <= 3 for i in range(len(levels)-1))
    
    return increasing or decreasing
        
with open('day-2/input.txt', 'r') as f:
    input_data = f.read().strip()
    
safe_reports = sum(1 for line in input_data.splitlines() if is_safe(line))
print(safe_reports)