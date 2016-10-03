# craps.py
# Casino Craps Game Simulation
'''
    Input: The program first prompt for and gets a number of games to simulate.
    Output: The program will provide a initial prompt as following:
     How many games to simulate?
    Then the program will print out the success rate of n craps games:
     Your winning rate is : 0.3
'''
from random import random, randrange
import time

def main():
    printIntroduction()
    n = getInput()
    rate = simNGames(n)
    printOut(rate)

def printIntroduction():
    print('This program simulate the Craps Game in Casino '\
          'and prints out the success rate that if you play.')

def getInput():
    # Return the number of games to simulate
    n = int(input('How many games to simulate? '))
    return n

def simNGames(n):
    # Simulates the n number of craps games in casino
    # Return the success rate of a player
    wins = 0
    for i in range(n):
        x = rollDice()
        if checkRoll(x):
            wins += 1
    rate = wins / n
    return rate


def rollDice():
    # Return a sum of two dices with random probability a
    x =  randrange(1,7) + randrange(1,7)
    return x

def checkRoll(x):
    # Check the player win or lose with the x sum of two dices
    # Return True if win, otherwise False
    if x in [2, 3, 12]:
        return False
    elif x in [7, 11]:
        return True
    else:
        while True:
            prob = random()
            y = rollDice()
            if y == x:
                return True
            elif y == 7:
                return False

def printOut(rate):
    print('Your success rate is {}.'.format(rate))

if __name__ == '__main__':
    startTime = time.time()
    main()
    print('{:.5f} seconds'.format(time.time() - startTime))
