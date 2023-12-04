file = open('input.txt', 'r')
file = file.read().split('\n')
p1 = 0
p2 = 0

for i, game in enumerate(file):
    gameList = []
    redCubes = []
    blueCubes = []
    greenCubes = []
    redTrue = True
    blueTrue = True
    greenTrue = True
    redMax = 0
    blueMax = 0
    greenMax = 0
    game = game.replace(' ', '').split(':').pop(1).split(';')

    for roll in game:
        roll = roll.split(',')
        gameList.append(roll)

    for j, cubes in enumerate(gameList):
        for k in gameList[j]:
            if 'red' in k:
                redCubes.append(int(''.join(filter(str.isdigit, k))))
            if 'blue' in k:
                blueCubes.append(int(''.join(filter(str.isdigit, k))))
            if 'green' in k:
                greenCubes.append(int(''.join(filter(str.isdigit, k))))

    # part one
    for element in redCubes:
        if int(element) > 12:
            redTrue = False
    for element in blueCubes:
        if int(element) > 14:
            blueTrue = False
    for element in greenCubes:
        if int(element) > 13:
            greenTrue = False

    if redTrue and blueTrue and greenTrue:
        p1 += i + 1

    # part two
    redMax = max(redCubes)
    blueMax = max(blueCubes)
    greenMax = max(greenCubes)

    p2 += redMax * blueMax * greenMax

print(p1)
print(p2)