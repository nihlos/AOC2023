file = open('input.txt', 'r')
file = file.read().split('\n')

numberList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
sum = 0

for line in file:
    digitList = []
    for i, character in enumerate(line):
        if character.isdigit():
            digitList.append(character)

        for j, number in enumerate(numberList):
            if line[i:].startswith(number):
                digitList.append(str(j + 1))

    sum += int(digitList[0] + digitList[-1])

print(sum)
