import re
file = open('input.txt', 'r')
file = file.read().split('\n')

copiesList = []
instanceList = []

p1 = 0
p2 = 0

# p1
for i in range(len(file)):
    line = file[i].split(':', 1).pop(1)
    numbersLists = line.split('|')
    winner = 0
    copies = 0

    # creates list containing numbers
    for j in range(len(numbersLists)):
        numbersLists[j] = re.findall(r'\d+', numbersLists[j])

    # number is match then add points
    for number in numbersLists[1]:
        if number in numbersLists[0]:
            if winner == 0:
                winner += 1
            else:
                winner *= 2
            copies += 1

    copiesList.append(copies)
    instanceList.append(1)
    p1 += winner


# p2
for i in range(len(instanceList)):
    for j in range(instanceList[i]):
        copy = copiesList[i]
        for k in range(copy):
            instanceList[i + k + 1] += 1

for i in range(len(instanceList)):
    p2 += instanceList[i]

print(p1)
print(p2)
