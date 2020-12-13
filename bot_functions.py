#!/usr/bin/env python3
import random


def passwordgen():
    # print('Erstellt ein sicheres und leicht zu merkendes Passwort')
    # loads all the languages words, numbers and special characters into lists
    words = [line.rstrip('\n') for line in open("deutsch.txt")]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    special = ["!", "§", "$", "%", "&", "=", "?", "+", "#", "-", "*"]

    # chooses 3 random words
    part0 = random.choice(words)
    part1 = random.choice(words)
    part2 = random.choice(words)

    # chooses the supplicants (1 number, 1 special char and determines their position)
    if random.randint(0, 1) == 0:
        supp0 = str(random.choice(numbers))
        supp1 = random.choice(special)
    else:
        supp0 = random.choice(special)
        supp1 = str(random.choice(numbers))

    # assembling everything into one string and printing
    password = part0 + supp0 + part1 + supp1 + part2
    # print(password)
    return password


def diceroll(diceInput):
    #print('please enter the Dice you want to roll in the Format ndx,')
    #print('where n is the count of dices, and x is the number of possible values of the dice, e.g. 2d6')
    diceRaw = diceInput
    diceList = diceRaw.split("d")
    diceFaces = int(diceList[1])
    diceCount = int(diceList[0])
    diceOut = 0
    i = 0

    while i < diceCount:
        diceResult: int = random.randint(1, diceFaces)
        diceOut: int = diceOut + diceResult
        i += 1

    return diceOut
