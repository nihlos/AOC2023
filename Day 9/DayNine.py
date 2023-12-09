import re, math
file = open('input.txt', 'r').read().split('\n')

p1 = 0
p2 = 0

for line in file:
    notZero = True
    historyList = [[int(j) for j in re.findall(r'-?\d+', line)]]

    # find extrapolation
    while notZero:
        historyList.append([])

        for i in range(len(historyList[-2]) - 1):
            firstValue = historyList[-2][i + 1]
            secondValue = historyList[-2][i]
            historyList[-1].append(firstValue - secondValue)

        if historyList[-1].count(0) == len(historyList[-1]):
            notZero = False

    # p1
    for list in historyList:
        p1 += list[len(list) - 1]

    first = historyList[len(historyList) - 1][0]
    for i in range(len(historyList)):
        first = historyList[len(historyList) - 1 - i][0] - first

    p2 += first

print(p1)
print(p2)
