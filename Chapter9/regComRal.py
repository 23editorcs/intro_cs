# regComRal.py
# Regular Volley Ball Compares to Rally Volleyball

'''
    Input: The program first promps for and gets the service probabilities of
     the two teams (called TeamA, TeamB). Then the program prompts for and
     gets the number of games to be simulated.
    Output: The program will provide a series of initial prompts such as
     the following:
      What is the prob. Team A wins a serve?
      What is the prob. Team B wins a serve?
      How many games to simulate?
     Then program will print out a nicly formatted report showing the
     number of games simulated and the number of wins and winning percentage
     for each team in both Regular and Rally. Here is an example:
     Games Simulated: 1000
     Regular Volleyball:
      Wins for Team A: 600
      Wins for Team B: 400
     Rally Volleyball:
      Wins for Team A: 550
      Wins for Team B: 450
     The change of each team in Rally Volleyball:
      The Rally Volleyball has magnified Team B wins.
      The Rally Volleyball has reduced Team A wins.
'''
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsAReg, winsBReg, winsARal, winsBRal = simNGames(n, probA, probB)
    printOut(winsAReg, winsBReg, winsARal, winsBRal)

def printIntro():
    print('This program simulates a game of regular and rally volleyball ' \
          'between two team called "A" and "B". The abilities of each team is'\
          ' indicated by a probability (a number between 0 and 1) that'\
          ' the team wins when serving. Team A always'\
          ' has the first serve.')
    
def getInputs():
    # Return the tree simulation parameters
    probA = float(input('What is the prob. Team A wins a serve? '))
    probB = float(input('What is the prob. Team B wins a serve? '))
    n = int(input('How many games to simulate? '))
    return probA, probB, n

def simNGames(n, probA, probB):
    # Simulates n games of volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Return number of wins for A and B.
    winsAReg = winsBReg = winsARal = winsBRal = 0
    for i in range(n):
        scoreA, scoreB = simOneRegGame(probA, probB)
        if scoreA > scoreB:
            winsAReg += 1
        else:
            winsBReg += 1
    for i in range(n):
        scoreA, scoreB = simOneRalGame(probA, probB)
        if scoreA > scoreB:
            winsARal += 1
        else:
            winsBRal += 1
    return winsAReg, winsBReg, winsARal, winsBRal
    
def simOneRegGame(probA, probB):
    # Simulates one regular game of volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = 'A'
    scoreA = scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = 'A'
    return scoreA, scoreB

def simOneRalGame(probA, probB):
    # Simulates one rally game of volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = 'A'
    scoreA = scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serving = 'B'
                scoreB += 1
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = 'A'
                scoreA += 1
    return scoreA, scoreB

def gameOver(a, b):
    # a, b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    return (a >= 21 or b >= 21) and (abs(a-b) > 1)

    
def printOut(winsAReg, winsBReg, winsARal, winsBRal):
    # Prints a summary of wins for each team
    n = winsAReg + winsBReg
    if winsARal > winsAReg:
        consA = 'magnified'
        consB = 'reduced'
    elif winsARal == winsAReg:
        consA = consB = 'no effect'
    else:
        consA = 'reduced'
        consB = 'magnified'
    
    print('\nGames Simulated: {}'.format(n))
    print('\nRegular Volleyball: \n' \
              'Wins for Team A: {0} ({1:.1%}) \n' \
              'Wins for Team B: {2} ({3:.1%}) \n' \
          .format(winsAReg, winsAReg/n, winsBReg, winsBReg/n))
    print('Rally Volleyball: \n' \
              'Wins for Team A: {0} ({1:.1%}) \n' \
              'Wins for Team B: {2} ({3:.1%}) \n' \
          .format(winsARal, winsARal/n, winsBRal, winsBRal/n))
    print('The change of each team in Rally Volley Ball: \n' \
              'The rally has {0} winning games of Team A. \n' \
              'The rally has {1} winning games of Team B. \n' \
          .format(consA, consB))
          
    
if __name__ == '__main__':
    main()
