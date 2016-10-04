# fiveAKind.py
# Simulation The 5 dices

from random import randrange
import time

def main():
    printIntro()
    n = getInput()
    prob = simNGame(n)
    printOutput(prob, n)

def printIntro():
    print('This program simulates rolling 5 six-sides dices, and '\
          'estimate the probability to 5 dices show the same number.')

def getInput():
    # Return the n number of games
    n = int(input('How many games to simulate? '))
    return n

def simNGame(n):
    # Simulate the n number of game which roll 5 dices
    # Return the probability of 5 dices show same side
    prob = 0
    for i in range(n):
        check = simOneGame()
        if check:
            prob += 1
    return prob

def simOneGame():
    # Generate the first roll
    x = randrange(1, 7)
    # Check the remain rolls is the same
    for i in range(4):
        y = randrange(1, 7)
        if y == x:
            check = True
        else:
            check = False
            break
    return check

def printOutput(prob, n):
    print('The prob of 5 same number in {0} games is {1:.2f}.'.format(n, prob/n))
    print('Other formula (1/6) ** 5 * n = {0}'.format(n * ((1/6)**5)))
    
if __name__ == '__main__':
    startTime = time.time()
    main()
    print('{:4f}'.format(time.time() - startTime))
