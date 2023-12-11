# using this to find the lowest common multiple amongst all steps to Z for p2
from math import lcm

file = open('input.txt','r').read().split('\n')

instructions = file[0]
del file[0]
del file[0]

# p1
keys = []
left = []
right = []

# p2
keysA = []
stepsZ = []

# answer
p1, p2 = 0, 1


# create lists
for i in range(len(file)):
    keys.append(file[i].split(' = ').pop(0))
    left.append(file[i].split(' = ').pop(1).split(', ').pop(0).replace('(', ''))
    right.append(file[i].split(' = ').pop(1).split(', ').pop(1).replace(')', ''))
    if file[i].split(' = ').pop(0)[2] == 'A':
        keysA.append(file[i].split(' = ').pop(0))


# p1
found = True
first = True
while found:
    if first:
        key = keys.index('AAA')
    for direction in instructions:
        if direction == 'L':
            key = int(keys.index(left[key]))
        if direction == 'R':
           key = int(keys.index(right[key]))

        if keys[key] == 'ZZZ':
            found = False
        p1 += 1

    first = False


# p2
for key in keysA:
    i, steps = 0, 0
    while not key.endswith('Z'):
        if instructions[i] == 'L':
            key = left[keys.index(key)]
        if instructions[i] == 'R':
            key = right[keys.index(key)]

        i += 1
        steps += 1

        if i > len(instructions) - 1:
            i = 0

    stepsZ.append(steps)


# this took hours to realize, since brute forcing didn't seem possible
for step in stepsZ:
    p2 = lcm(p2, step)

print(p1)
print(p2)
