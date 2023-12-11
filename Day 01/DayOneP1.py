file = open('input.txt', 'r')
file = file.read().split('\n')

firstNumber = ''
secondNumber = ''
numberList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum = 0

for i in range(len(file)):
    for j in range(len(file[i])):
        if firstNumber == '' and file[i][j] in numberList:
            firstNumber = file[i][j]

        if secondNumber == '' and file[i][::-1][j] in numberList:
            secondNumber = file[i][::-1][j]

    sum += int(firstNumber + secondNumber)
    firstNumber = ''
    secondNumber = ''

print(sum)
