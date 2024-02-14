#!/bin/python3

fourDigitNumbers = [i for i in range(1111,10000)]

noZeroFourDigitNumbers = [i for i in fourDigitNumbers if "0" not in str(i)]

uniqueFourDigitNumbers = []

for i in noZeroFourDigitNumbers:
    amount = [0 for _ in range(9)]
    for j in str(i):
        amount[int(j)-1] += 1

    works = True
    for j in amount:
        if j > 1:
            works = False

    if works:
        uniqueFourDigitNumbers.append(i)

pairs = []

for i in uniqueFourDigitNumbers:
    for j in uniqueFourDigitNumbers:
        works = True
        for k in range(len(str(i))):
            if str(i)[k] in str(j):
                works = False
                break
            else:
                continue

        if works:
            pairs.append([i, j])

digits = "123456789"

for pair in pairs:
    shoudEqual = 0
    for i in digits:
        if i not in str(pair[0])+str(pair[1]):
            shoudEqual = int(i)
            break

    if pair[0] / pair[1] == shoudEqual:
        print(f'Found one! It\'s {pair[0]}/{pair[1]}, which is equal to {shoudEqual}')
