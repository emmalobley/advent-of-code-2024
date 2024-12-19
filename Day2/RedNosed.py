def getReports(file):
    with open(file) as f:
        reports = [(x.split()) for x in f]
    return reports

def safeIncrease(report):
    for i in range(len(report)-1):
        if int(report[i]) > int(report[i+1]):
            return 0
        elif int(report[i]) < int(report[i+1]) - 3:
            return 0
        elif int(report[i]) == int(report[i + 1]):
            return 0
    return 1

def safeDecrease(report):
    for i in range(len(report)-1):
        if int(report[i]) < int(report[i+1]):
            return 0
        elif int(report[i]) > int(report[i+1]) + 3:
            return 0
        elif int(report[i]) == int(report[i+1]):
            return 0
    return 1

def checkSafe(report):
    return safeDecrease(report) + safeIncrease(report)

def safeDampened(report):
    for i in range(len(report)):
        newReport = report[:]  # slice notation - copy list
        newReport.pop(i)

        if checkSafe(newReport) == 1:
            return 1
    return 0

reports = getReports('input.txt')
safeCount = 0
for item in reports:
    isSafe = checkSafe(item)
    if isSafe == 0:
        isSafe = safeDampened(item)
    safeCount = safeCount + isSafe
print(safeCount)
