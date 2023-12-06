import re
file = open('input.txt', 'r')
file = file.read().split('\n')

time = [int(j) for j in re.findall(r'\d+', file[0].split('Time:').pop(1))]
distance = [int(j) for j in re.findall(r'\d+', file[1].split('Distance:').pop(1))]

raceTime = int(file[0].split('Time:').pop(1).replace(' ', ''))
raceDistance = int(file[1].split('Distance:').pop(1).replace(' ', ''))

p1 = 1

# p1
for i in range(len(time)):
    margin = 0
    count = 1

    for j in range(time[i]):
        start = count
        end = time[i] - count

        if start * end > distance[i]:
            margin += 1

        count += 1

    if margin != 0:
        p1 *= margin

# p2
margin = 0
count = 1
for i in range(raceTime):
    start = count
    end = raceTime - count

    if start * end > raceDistance:
        margin += 1

    # check progress
    # brute forcing cuz lazy
    print(str(i) + '/' + str(raceTime))
    count += 1

print(p1)
print(margin)
