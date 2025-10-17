from random import random
from enum import IntEnum

class Choice(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

playerOneWins = 0
machineWins = 0
draws = 0

def count():
    print(f"- - Player 1: {playerOneWins}, Machine: {machineWins}, Draws: {draws} - -")

exit = False  # Engineering Intensifies
while not exit:
    
    playerOne = int(input('Player One, enter your choice (0: rock, 1: paper, 2: scissors, 3: exit): '))
    if playerOne == 3:
        exit = True
        continue

    playerTwo = random.choice([0, 1, 2])

    if playerOne == playerTwo:
        draws += 1
        print("It's a draw!")
        count()
    elif (playerOne == Choice.ROCK and playerTwo == Choice.SCISSORS) or (playerOne == Choice.PAPER and playerTwo == Choice.ROCK) or (playerOne == Choice.SCISSORS and playerTwo == Choice.PAPER):
        playerOneWins += 1
        print("Player One wins this round!")
        count()
    else:
        machineWins += 1
        print("Machine wins this round!")
        count()