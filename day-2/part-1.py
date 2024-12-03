with open('day-2/input.txt', 'r') as f:
    input = f.read()

    # calculate number of safe reports
    safeReports = 0
    for line in input.split('\n'):
        lastLevel = -1
        graduallyIncreasing = True
        graduallyDecreasing = True
        safe = True
        for level in line.split(' '):
            # sanitizing input
            if not level.isnumeric():
                safe = False
                break

            # skip first iteration since at least 2 numbers are required
            if lastLevel == -1:
                lastLevel = int(level)
                continue

            # check for gradually increasing/decreasing
            if int(level) <= lastLevel:
                graduallyIncreasing = False
            
            if int(level) >= lastLevel:
                graduallyDecreasing = False
            
            # check that increase/decrease is at least 1 and at most 3
            difference = abs(int(level) - lastLevel)
            if difference > 3 or difference < 1:
                graduallyIncreasing = False
                graduallyDecreasing = False

            # final check for whether report is safe
            if not graduallyIncreasing and not graduallyDecreasing:
                safe = False
                break

            lastLevel = int(level)

        if safe:
            safeReports += 1

    # output number of safe reports
    print(safeReports)