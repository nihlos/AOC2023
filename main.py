file = open('input.txt', 'r')
file = file.read().split('\n')

p1 = 0
p2 = 0

for i in range(len(file)):
    # p1 var
    previousLine = []
    currentLine = []
    nextLine = []
    digitIndex = []
    tempList = []
    matchList = []

    # p2 var
    asteriskIndex = []
    historyIndex = []
    previousNumbers = []
    currentNumbers = []
    nextNumbers = []

    # get indexes of digits and special characters
    for j in range(len(file[i])):
        if file[i][j].isdigit():
            digitIndex.append(j)

        if file[i][j] == '*':
            asteriskIndex.append(j)

    # previous line
    if i != 0:
        for j in range(len(file[i - 1])):
            if file[i - 1][j] != '.' and file[i - 1][j] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                previousLine.append(j)

            if file[i - 1][j] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                previousNumbers.append(j)

    # current line
    for j in range(len(file[i])):
        if file[i][j] != '.' and file[i][j] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            currentLine.append(j)

        if file[i][j] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            currentNumbers.append(j)

    # nextLine
    if i != len(file) - 1:
        for j in range(len(file[i - 1])):
            if file[i + 1][j] != '.' and file[i + 1][j] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                nextLine.append(j)

            if file[i + 1][j] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                nextNumbers.append(j)

    historyIndex.append(previousNumbers)
    historyIndex.append(currentNumbers)
    historyIndex.append(nextNumbers)

    # p1 adjacent logic
    for digit in digitIndex:

        # previous
        for index in previousLine:
            if digit == index - 1 or digit == index or digit == index + 1:
                matchList.append(digit)

        # current
        for index in currentLine:
            if digit == index - 1 or digit == index or digit == index + 1 and digit not in matchList:
                matchList.append(digit)

        # next
        for index in nextLine:
            if digit == index - 1 or digit == index or digit == index + 1 and digit not in matchList:
                matchList.append(digit)

    # p1 cleanup repeat matches
    for j in range(len(matchList)):
        try:
            if matchList[j + 1] == matchList[j] + 1:
                tempList.append(matchList[j + 1])
        except:
            pass

    for index in tempList:
        matchList.remove(index)

    # p1 completes digits
    for match in matchList:
        count = 1
        digit = file[i][match]
        while file[i][match - count] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            digit = file[i][match - count] + digit
            count += 1

        count = 1
        try:
            while file[i][match + count] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                digit = digit + file[i][match + count]
                count += 1
        except:
            pass

        p1 += int(digit)


    # p2 logic
    for asterisk in asteriskIndex:
        adjacentIndex = []
        adjacentNumbers = []

        # gets adjacent indexes
        for list in historyIndex:
            indexList = []
            for index in list:
                if asterisk == index - 1 or asterisk == index or asterisk == index + 1:
                    indexList.append(index)
            adjacentIndex.append(indexList)

        # remove repeat matches
        for j in range(len(adjacentIndex)):
            tempList = []
            for k in range(len(adjacentIndex[j])):
                try:
                    if adjacentIndex[j][k + 1] == adjacentIndex[j][k] + 1:
                        tempList.append(adjacentIndex[j][k + 1])
                except:
                    pass
            try:
                for index in tempList:
                    adjacentIndex[j].remove(index)
            except:
                pass

        # complete digits
        for j in range(len(adjacentIndex)):
            for k in range(len(adjacentIndex[j])):

                # previous
                if j == 0 and i != 0:
                    count = 1
                    digit = file[i - 1][adjacentIndex[j][k]]
                    while file[i - 1][adjacentIndex[j][k] - count] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        digit = file[i - 1][adjacentIndex[j][k] - count] + digit
                        count += 1

                    count = 1
                    try:
                        while file[i - 1][adjacentIndex[j][k] + count] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            digit = digit + file[i - 1][adjacentIndex[j][k] + count]
                            count += 1
                    except:
                        pass

                    adjacentNumbers.append(digit)

                # current
                if j == 1:
                    count = 1
                    digit = file[i][adjacentIndex[j][k]]
                    while file[i][adjacentIndex[j][k] - count] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        digit = file[i][adjacentIndex[j][k] - count] + digit
                        count += 1

                    count = 1
                    try:
                        while file[i][adjacentIndex[j][k] + count] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            digit = digit + file[i][adjacentIndex[j][k] + count]
                            count += 1
                    except:
                        pass

                    adjacentNumbers.append(digit)

                # next
                if j == 2 and i != len(file) - 1:
                    count = 1
                    digit = file[i + 1][adjacentIndex[j][k]]
                    while file[i + 1][adjacentIndex[j][k] - count] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        digit = file[i + 1][adjacentIndex[j][k] - count] + digit
                        count += 1

                    count = 1
                    try:
                        while file[i + 1][adjacentIndex[j][k] + count] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            digit = digit + file[i + 1][adjacentIndex[j][k] + count]
                            count += 1
                    except:
                        pass

                    adjacentNumbers.append(digit)

        if len(adjacentNumbers) == 2:
            p2 += int(adjacentNumbers[0]) * int(adjacentNumbers[1])


print(p1)
print(p2)
