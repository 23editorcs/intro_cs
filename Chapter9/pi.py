# pi.py
# Calculation pi with Monte Carlo
'''
    Input: The program prompt for and gets the number of game
     to be simulated.
    Output: The program prints out the pi calculated by Monte Carlo approach
'''

from random import random
import time

def main():
    printIntro()
    n = getInput()
    pi = simNThrown(n)
    printOutput(pi)

def printIntro():
    print('This program simulates the Monte Carlo experiment'\
          ' and calculates pi number with this method.')

def getInput():
    # Return the n number of games to be simulated
    n = int(input('How many games to simulate? '))
    return n

def simNThrown(n):
    # Simulates the n number of throwing to the dart board.
    # Calculate the pi number with formula pi = 4(h/n)
    # which h is the number of time the dart inside the board.
    h = 0
    for i in range(n):
        board = simOneThrown()
        if board:
            h += 1
    pi = 4 * (h / n)
    return pi

def simOneThrown():
    # Simulates One Throwing Game
    # Return True if the dart inside the board, otherwise False
    board = False
    # Get the coordinates of x and y after threw the dart
    x, y = throwDart()
    # Check the dart inside the board
    if checkDart(x, y):
        board = True
    return board

def throwDart():
    # Simulates the throw active
    # Return coordinates of x and y
    x = 2 * random() - 1.0
    y = 2 * random() - 1.0
    return x, y

def checkDart(x, y):
    # Check the dart is inside the board (0,0), r = 1
    # Return True if inside, otherwise False
    if x**2 + y**2 <= 1:
        return True
    else: return False

def printOutput(pi):
    print('The approximate pi number by Monte Carlo is {:.4f}.'.format(pi))
    
if __name__ == '__main__':
    startTime = time.time()
    main()
    print('{:.4f}'.format(time.time() - startTime))
