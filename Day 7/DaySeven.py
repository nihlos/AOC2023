import time
file = open('input.txt', 'r')
file = file.read().split('\n')

cards = []
bet = []
faces = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

# types
fiveKind = []
fourKind = []
fullHouse = []
threeKind = []
twoPair = []
onePair = []
highCard = []

# p2 var
cards2 = []
faces2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
fiveKind2 = []
fourKind2 = []
fullHouse2 = []
threeKind2 = []
twoPair2 = []
onePair2 = []
highCard2 = []

p1 = 0
p2 = 0

# initial lists
for i in range(len(file)):
    cards.append(file[i].split(' ').pop(0))
    bet.append(int(file[i].split(' ').pop(1)))

# p1
# get types
for card in cards:
    FH = True
    TP = True
    type = 0
    finalType = 0

    for face in faces:
        otherFaces = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        otherFaces.remove(face)

        if card.count(face) == 5:
            type = 7

        elif card.count(face) == 4:
            type = 6

        elif card.count(face) == 3:
            for other in otherFaces:
                if card.count(other) == 2:
                    type = 5
                    FH = False

            if FH:
                type = 4

        elif card.count(face) == 2:
            for other in otherFaces:
                if card.count(other) == 2:
                    type = 3
                    TP = False

            if TP:
                type = 2

        else:
            if card.count(face) == 1:
                type = 1

        if type > finalType:
            finalType = type

    if finalType == 7:
        fiveKind.append(card)
    if finalType == 6:
        fourKind.append(card)
    if finalType == 5:
        fullHouse.append(card)
    if finalType == 4:
        threeKind.append(card)
    if finalType == 3:
        twoPair.append(card)
    if finalType == 2:
        onePair.append(card)
    if finalType == 1:
        highCard.append(card)

sort_order = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}

# sort lists
fiveKind.sort(key=lambda x: [sort_order[c] for c in x])
fourKind.sort(key=lambda x: [sort_order[c] for c in x])
fullHouse.sort(key=lambda x: [sort_order[c] for c in x])
threeKind.sort(key=lambda x: [sort_order[c] for c in x])
twoPair.sort(key=lambda x: [sort_order[c] for c in x])
onePair.sort(key=lambda x: [sort_order[c] for c in x])
highCard.sort(key=lambda x: [sort_order[c] for c in x])

count = len(cards)
for card in fiveKind:
    p1 += bet[cards.index(card)] * count
    count -= 1
for card in fourKind:
    p1 += bet[cards.index(card)] * count
    count -= 1
for card in fullHouse:
    p1 += bet[cards.index(card)] * count
    count -= 1
for card in threeKind:
    p1 += bet[cards.index(card)] * count
    count -= 1
for card in twoPair:
    p1 += bet[cards.index(card)] * count
    count -= 1
for card in onePair:
    p1 += bet[cards.index(card)] * count
    count -= 1
for card in highCard:
    p1 += bet[cards.index(card)] * count
    count -= 1


# p2
# get types
for card in cards:
    FH = True
    TP = True
    type = 0
    finalType = 0

    for face in faces2:
        tempCard = card
        tempCard = tempCard.replace('J', face)
        otherFaces = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        otherFaces.remove(face)

        if tempCard.count(face) == 5:
            type = 7

        elif tempCard.count(face) == 4:
            type = 6

        elif tempCard.count(face) == 3:
            for other in otherFaces:
                if tempCard.count(other) == 2:
                    type = 5
                    editedCard = tempCard
                    FH = False

            if FH:
                type = 4

        elif tempCard.count(face) == 2:
            for other in otherFaces:
                if tempCard.count(other) == 2:
                    type = 3
                    TP = False

            if TP:
                type = 2

        else:
            if tempCard.count(face) == 1:
                type = 1

        if type > finalType:
            finalType = type
            editedCard = tempCard

    if finalType == 7:
        if 'J' in card:
            fiveKind2.append(editedCard + 'P:' + str(cards.index(card)))
        else:
            fiveKind2.append(editedCard + ':' + str(cards.index(card)))
    if finalType == 6:
        if 'J' in card:
            fourKind2.append(editedCard + 'P:' + str(cards.index(card)))
        else:
            fourKind2.append(editedCard + ':' + str(cards.index(card)))
    if finalType == 5:
        if 'J' in card:
            fullHouse2.append(editedCard + 'P:' + str(cards.index(card)))
        else:
            fullHouse2.append(editedCard + ':' + str(cards.index(card)))
    if finalType == 4:
        if 'J' in card:
            threeKind2.append(editedCard + 'P:' + str(cards.index(card)))
        else:
            threeKind2.append(editedCard + ':' + str(cards.index(card)))
    if finalType == 3:
        if 'J' in card:
            twoPair2.append(editedCard + 'P:' + str(cards.index(card)))
        else:
            twoPair2.append(editedCard + ':' + str(cards.index(card)))
    if finalType == 2:
        if 'J' in card:
            onePair2.append(editedCard + 'P:' + str(cards.index(card)))
        else:
            onePair2.append(editedCard + ':' + str(cards.index(card)))
    if finalType == 1:
        if 'J' in card:
            highCard2.append(editedCard + 'P:' + str(cards.index(card)))
        else:
            highCard2.append(editedCard + ':' + str(cards.index(card)))


sort_order = {'A': 0, 'K': 1, 'Q': 2, 'T': 3, '9': 4, '8': 5, '7': 6, '6': 7, '5': 8, '4': 9, '3': 10, '2': 11, 'P': 12}

# sort lists
fiveKind2.sort(key=lambda x: [sort_order[c] for c in x.split(':').pop(0)])
fourKind2.sort(key=lambda x: [sort_order[c] for c in x.split(':').pop(0)])
fullHouse2.sort(key=lambda x: [sort_order[c] for c in x.split(':').pop(0)])
threeKind2.sort(key=lambda x: [sort_order[c] for c in x.split(':').pop(0)])
twoPair2.sort(key=lambda x: [sort_order[c] for c in x.split(':').pop(0)])
onePair2.sort(key=lambda x: [sort_order[c] for c in x.split(':').pop(0)])
highCard2.sort(key=lambda x: [sort_order[c] for c in x.split(':').pop(0)])

print(cards2)

# get sum
count = len(cards)
for card in fiveKind2:
    print(card)
    print(count)
    print(bet[int(card.split(':').pop(1))])
    p2 += bet[int(card.split(':').pop(1))] * count
    count -= 1
for card in fourKind2:
    p2 += bet[int(card.split(':').pop(1))] * count
    count -= 1
for card in fullHouse2:
    p2 += bet[int(card.split(':').pop(1))] * count
    count -= 1
for card in threeKind2:
    p2 += bet[int(card.split(':').pop(1))] * count
    count -= 1
for card in twoPair2:
    p2 += bet[int(card.split(':').pop(1))] * count
    count -= 1
for card in onePair2:
    p2 += bet[int(card.split(':').pop(1))] * count
    count -= 1
for card in highCard2:
    p2 += bet[int(card.split(':').pop(1))] * count
    count -= 1

print(fiveKind2)
print(fourKind2)
print(fullHouse2)
print(threeKind2)
print(twoPair2)
print(onePair2)
print(highCard2)
print(p1)
print(p2)
