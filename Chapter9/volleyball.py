# volleyball.py
# Volleyball Simulation

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
     for each team. Here is an example:
      Games Simulated: 1000
      Wins for A: 600 (60%)
      Wins for B: 400 (40%)
'''
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printOut(winsA, winsB)

def printIntro():
    print('This program simulates a game of volleyball between two'\
          'team called "A" and "B". The abilities of each team is'\
          'indicated by a probability (a number between 0 and 1) that'\
          'the team wins the point when serving. Team A always'\
          'has the first serve.')
    
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
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates one game of volleyball between teams whose
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

def gameOver(a, b):
    # a, b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    return (a >= 15 or b >= 15) and (abs(a-b) > 1)

def testGameOver():
    print(gameOver(0,0) == False)
    print(gameOver(15, 15) == False)
    print(gameOver(15, 13) == True)
    print(gameOver(13, 15) == True)
    print(gameOver(15, 14) == False)
    print(gameOver(14, 15) == False)
    print(gameOver(15, 17) == True)
    print(gameOver(16, 17) == False)
    
def printOut(winsA, winsB):
    # Prints a summary of wins for each team
    n = winsA + winsB
    print('Games Simulated: {0} \n'\
          'Wins for Team A: {1} \n'\
          'Wins for Team B: {2} \n'\
          .format(n, winsA, winsB))
          
    
if __name__ == '__main__':
    main()
