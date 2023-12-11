import re
file = open('input.txt', 'r')
file = file.read().split('\n')

seeds = []
seedRanges = []

soil = []
fertilizer = []
water = []
light = []
temperature = []
humidity = []
location = []

p1 = 0
p2 = 0

# initialize lists
for i in range(len(file)):

    # seeds
    if i == 0:
        seeds = [int(j) for j in re.findall(r'\d+', file[i].split('seeds: ').pop(1))]
        seedRanges = [int(j) for j in re.findall(r'\d+', file[i].split('seeds: ').pop(1))]

    # soil
    if file[i] == 'seed-to-soil map:':
        count = i + 1
        while file[count] != 'soil-to-fertilizer map:' and file[count] != '':
            soil.append([int(j) for j in re.findall(r'\d+', file[count])])
            count += 1

    # fertilizer
    if file[i] == 'soil-to-fertilizer map:':
        count = i + 1
        while file[count] != 'fertilizer-to-water map:' and file[count] != '':
            fertilizer.append([int(j) for j in re.findall(r'\d+', file[count])])
            count += 1

    # water
    if file[i] == 'fertilizer-to-water map:':
        count = i + 1
        while file[count] != 'water-to-light map:' and file[count] != '':
            water.append([int(j) for j in re.findall(r'\d+', file[count])])
            count += 1

    # light
    if file[i] == 'water-to-light map:':
        count = i + 1
        while file[count] != 'light-to-temperature map:' and file[count] != '':
            light.append([int(j) for j in re.findall(r'\d+', file[count])])
            count += 1

    # temperature
    if file[i] == 'light-to-temperature map:':
        count = i + 1
        while file[count] != 'temperature-to-humidity map:' and file[count] != '':
            temperature.append([int(j) for j in re.findall(r'\d+', file[count])])
            count += 1

    # humidity
    if file[i] == 'temperature-to-humidity map:':
        count = i + 1
        while file[count] != 'humidity-to-location map:' and file[count] != '':
            humidity.append([int(j) for j in re.findall(r'\d+', file[count])])
            count += 1

    # location
    if file[i] == 'humidity-to-location map:':
        count = i + 1
        while count < len(file):
            location.append([int(j) for j in re.findall(r'\d+', file[count])])
            count += 1


# p1: logic to find locations
for i in range(len(seeds)):
    tempValue = 0

    # soil
    for map in soil:
        destination = map[0]
        source = map[1]
        length = map[2] - 1

        # is the seed between the source and the source + range (named length to avoid shadowing)
        if source <= seeds[i] <= source + length:
            tempValue = destination + seeds[i] - source

    seeds[i] = tempValue

    # fertilizer
    for map in fertilizer:
        destination = map[0]
        source = map[1]
        length = map[2] - 1

        if source <= seeds[i] <= source + length:
            tempValue = destination + seeds[i] - source

    seeds[i] = tempValue

    # water
    for map in water:
        destination = map[0]
        source = map[1]
        length = map[2] - 1

        if source <= seeds[i] <= source + length:
            tempValue = destination + seeds[i] - source

    seeds[i] = tempValue

    # light
    for map in light:
        destination = map[0]
        source = map[1]
        length = map[2] - 1

        if source <= seeds[i] <= source + length:
            tempValue = destination + seeds[i] - source

    seeds[i] = tempValue

    # temperature
    for map in temperature:
        destination = map[0]
        source = map[1]
        length = map[2] - 1

        if source <= seeds[i] <= source + length:
            tempValue = destination + seeds[i] - source

    seeds[i] = tempValue

    # humidity
    for map in humidity:
        destination = map[0]
        source = map[1]
        length = map[2] - 1

        if source <= seeds[i] <= source + length:
            tempValue = destination + seeds[i] - source

    seeds[i] = tempValue

    # location
    for map in location:
        destination = map[0]
        source = map[1]
        length = map[2] - 1

        if source <= seeds[i] <= source + length:
            tempValue = destination + seeds[i] - source

    seeds[i] = tempValue


# p2: initialize seed ranges list | pairs items in list into sublists
tempList = []
for i in range(0, len(seedRanges), 2):
    tempList.append(seedRanges[i:i + 2])

seedRanges = tempList


# p2: logic to find locations
# brute forcing this because I can't figure it out otherwise
finalSeed = 9999999999999
for i in range(len(seedRanges)):
    for seed in range(seedRanges[i][0], seedRanges[i][0] + seedRanges[i][1]):
        originalSeed = seed
        tempValue = 0

        # soil
        for map in soil:
            destination = map[0]
            source = map[1]
            length = map[2] - 1

            if source <= seed <= source + length:
                tempValue = destination + seed - source

        seed = tempValue

        # fertilizer
        for map in fertilizer:
            destination = map[0]
            source = map[1]
            length = map[2] - 1

            if source <= seed <= source + length:
                tempValue = destination + seed - source

        seed = tempValue

        # water
        for map in water:
            destination = map[0]
            source = map[1]
            length = map[2] - 1

            if source <= seed <= source + length:
                tempValue = destination + seed - source

        seed = tempValue

        # light
        for map in light:
            destination = map[0]
            source = map[1]
            length = map[2] - 1

            if source <= seed <= source + length:
                tempValue = destination + seed - source

        seed = tempValue

        # temperature
        for map in temperature:
            destination = map[0]
            source = map[1]
            length = map[2] - 1

            if source <= seed <= source + length:
                tempValue = destination + seed - source

        seed = tempValue

        # humidity
        for map in humidity:
            destination = map[0]
            source = map[1]
            length = map[2] - 1

            if source <= seed <= source + length:
                tempValue = destination + seed - source

        seed = tempValue

        # location
        for map in location:
            destination = map[0]
            source = map[1]
            length = map[2] - 1

            if source <= seed <= source + length:
                tempValue = destination + seed - source

        seed = tempValue

        if seed < finalSeed:
            finalSeed = seed

        # progress check
        # only took like 20 hours of runtime to complete
        print(str(i) + ': ' + str(originalSeed) + ' - ' + str(seedRanges[i][0] + seedRanges[i][1]) + ' | ' + str(finalSeed))
        print()

print(min(seeds))
print(finalSeed)
