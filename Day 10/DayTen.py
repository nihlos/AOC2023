file = open('input.txt').read().split('\n')

# all possible pipes S could be
pipesS = ['|', '-', 'L', 'J', '7', 'F']
loopList = []

p2 = 0

# locate S
for i in range(len(file)):
    for pipe in file[i]:
        if pipe == 'S':
            lineS = i
            indexS = file[i].find('S')

# find loops and measure distance
for pipe in pipesS:
    currentLine = lineS
    currentIndex = indexS
    currentPipe = pipe

    isLoop = False
    contiuneLoop = True

    if pipe in ['|', 'L', 'J']:
        right = True
        left = False
        up = True
        down = False
    else:
        right = False
        left = True
        up = False
        down = True

    loopIndex = []
    loop = []
    while True:
        if currentPipe == '|':
            # up
            if file[currentLine - 1][currentIndex] in ['F', '7', '|', 'S'] and up:
                currentLine = currentLine - 1
                currentPipe = file[currentLine][currentIndex]
                loop.append(currentPipe)
                loopIndex.append([currentLine, currentIndex])

                if currentPipe == 'F':
                    right = True
                    left = False
                if currentPipe == '7':
                    left = True
                    right = False
                if currentPipe == 'S':
                    isLoop = True
                    loop[-1] = pipe
                    break
            # down
            elif file[currentLine + 1][currentIndex] in ['L', 'J', '|', 'S'] and down:
                currentLine = currentLine + 1
                currentPipe = file[currentLine][currentIndex]
                loop.append(currentPipe)
                loopIndex.append([currentLine, currentIndex])

                if currentPipe == 'L':
                    right = True
                    left = False
                if currentPipe == 'J':
                    left = True
                    right = False
                if currentPipe == 'S':
                    isLoop = True
                    loop[-1] = pipe
                    break

            else:
                break

        elif currentPipe == '-':
            # right
            if file[currentLine][currentIndex + 1] in ['J', '7', '-', 'S'] and right:
                currentIndex = currentIndex + 1
                currentPipe = file[currentLine][currentIndex]
                loop.append(currentPipe)
                loopIndex.append([currentLine, currentIndex])

                if currentPipe == 'J':
                    up = True
                    down = False
                if currentPipe == '7':
                    down = True
                    up = False
                if currentPipe == 'S':
                    isLoop = True
                    loop[-1] = pipe
                    break

            # left
            elif file[currentLine][currentIndex - 1] in ['L', 'F', '-', 'S'] and left:
                currentIndex = currentIndex - 1
                currentPipe = file[currentLine][currentIndex]
                loop.append(currentPipe)
                loopIndex.append([currentLine, currentIndex])

                if currentPipe == 'L':
                    up = True
                    down = False
                if currentPipe == 'F':
                    down = True
                    up = False
                if currentPipe == 'S':
                    isLoop = True
                    loop[-1] = pipe
                    break

            else:
                break

        elif currentPipe == 'L':
            # up
            if file[currentLine - 1][currentIndex] in ['F', '7', '|', 'S'] and up:
                currentLine = currentLine - 1
                currentPipe = file[currentLine][currentIndex]
                loop.append(currentPipe)
                loopIndex.append([currentLine, currentIndex])

                if currentPipe == 'F':
                    right = True
                    left = False
                if currentPipe == '7':
                    left = True
                    right = False
                if currentPipe == 'S':
                    isLoop = True
                    loop[-1] = pipe
                    break

            # right
            elif file[currentLine][currentIndex + 1] in ['J', '7', '-', 'S'] and right:
                currentIndex = currentIndex + 1
                currentPipe = file[currentLine][currentIndex]
                loop.append(currentPipe)
                loopIndex.append([currentLine, currentIndex])

                if currentPipe == 'J':
                    up = True
                    down = False
                if currentPipe == '7':
                    down = True
                    up = False
                if currentPipe == 'S':
                    isLoop = True
                    loop[-1] = pipe
                    break

            else:
                break

        elif currentPipe == 'J':
            # up
            if file[currentLine - 1][currentIndex] in ['F', '7', '|', 'S'] and up:
                currentLine = currentLine - 1
                currentPipe = file[currentLine][currentIndex]
                loop.append(currentPipe)
                loopIndex.append([currentLine, currentIndex])

                if currentPipe == 'F':
                    right = True
                    left = False
                if currentPipe == '7':
                    left = True
                    right = False
                if currentPipe == 'S':
                    isLoop = True
                    loop[-1] = pipe
                    break

            # left
            elif file[currentLine][currentIndex - 1] in ['L', 'F', '-', 'S'] and left:
                currentIndex = currentIndex - 1
                currentPipe = file[currentLine][currentIndex]
                loop.append(currentPipe)
                loopIndex.append([currentLine, currentIndex])

                if currentPipe == 'F':
                    down = True
                    up = False
                if currentPipe == 'L':
                    up = True
                    down = False
                if currentPipe == 'S':
                    isLoop = True
                    loop[-1] = pipe
                    break

            else:
                break

        elif currentPipe == '7':
            # down
            if file[currentLine + 1][currentIndex] in ['L', 'J', '|', 'S'] and down:
                currentLine = currentLine + 1
                currentPipe = file[currentLine][currentIndex]
                loop.append(currentPipe)
                loopIndex.append([currentLine, currentIndex])

                if currentPipe == 'J':
                    left = True
                    right = False
                if currentPipe == 'L':
                    right = True
                    left = False
                if currentPipe == 'S':
                    isLoop = True
                    loop[-1] = pipe
                    break

            # left
            elif file[currentLine][currentIndex - 1] in ['L', 'F', '-', 'S'] and left:
                currentIndex = currentIndex - 1
                currentPipe = file[currentLine][currentIndex]
                loop.append(currentPipe)
                loopIndex.append([currentLine, currentIndex])

                if currentPipe == 'F':
                    down = True
                    up = False
                if currentPipe == 'L':
                    up = True
                    down = False
                if currentPipe == 'S':
                    isLoop = True
                    loop[-1] = pipe
                    break

            else:
                break

        elif currentPipe == 'F':
            # down
            if file[currentLine + 1][currentIndex] in ['L', 'J', '|', 'S'] and down:
                currentLine = currentLine + 1
                currentPipe = file[currentLine][currentIndex]
                loop.append(currentPipe)
                loopIndex.append([currentLine, currentIndex])

                if currentPipe == 'J':
                    left = True
                    right = False
                if currentPipe == 'L':
                    right = True
                    left = False
                if currentPipe == 'S':
                    isLoop = True
                    loop[-1] = pipe
                    break

            # right
            elif file[currentLine][currentIndex + 1] in ['J', '7', '-', 'S'] and right:
                currentIndex = currentIndex + 1
                currentPipe = file[currentLine][currentIndex]
                loop.append(currentPipe)
                loopIndex.append([currentLine, currentIndex])

                if currentPipe == 'J':
                    up = True
                    down = False
                if currentPipe == '7':
                    down = True
                    up = False
                if currentPipe == 'S':
                    isLoop = True
                    loop[-1] = pipe
                    break

            else:
                break

        else:
            break

    if isLoop:
        loopList.append(loop)

# p1 find the furthest point in the pipes
length = 0
for loop in loopList:
    if len(loop) > length:
        length = len(loop)
        finalLoop = loop
