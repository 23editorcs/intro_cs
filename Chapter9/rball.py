# rball.py
# Simulation Racquetball

'''
    Input: The program first prompts for and gets the service probabilities of
     the two players (called PlayerA, PlayerB). Then the program prompts for
     and gets the number of games to be simulated.
    Output: The program will provide a series of initial prompts such as the
     following:
      What is the prob. player A wins a serve?
      What is the prob. player B wins a serve?
      How many games to simulate?
     Then program will print out a nicely formatted report showing the number
     of games simulated and the number of wins and winning percentage for
     each player. Here is an example:
      Games Simulated: 500
      Wins for A: 260 (52%)
      Wins for B: 240 (48%)
'''

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    print(winsA, winsB)
    printOutput(winsA, winsB)

def printIntro():
    # Print the introduction of the program
    print('This program simulates a game of racquetball between two')
    print('player called "A" and "B". The abilities of each player is')
    print('indicated by a probability (between 0 and 1) that')
    print('that the player wins a point when serving. Player A always')
    print('has the first serve.')
          
def getInputs():
    # Get the inputs from user, include prob. player A wins a serve
    # prob. player B wins a serve, number of games to simulate
    a = float(input('What is the prob. player A wins a serve?(0-1) '))
    b = float(input('What is the prob. player B wins a serve?(0-1) '))
    n = int(input('How many games to simulate? '))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulation n games. Calculate the win games of player A, player B.
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        print(scoreA, scoreB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players whose
    #   abilities are represented by the probability of winning a serve.
    # Return a final scores for A and B
    serving = 'A'
    scoreA = scoreB = 0
    while not GameOver(scoreA, scoreB):
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

def GameOver(scoreA, scoreB):
    # scoreA, scoreB represent scores for player a and b
    # return True if the game is over, otherwise return False
    return scoreA == 15 or scoreB == 15
    

def printOutput(winsA, winsB):
    # Print the result of simulation, Games Simulated, Wins for A, Wins for B
    n = winsA + winsB
    print('Simulated Games: {0} \n'\
          'Wins for A: {1} ({3:0.1%}) \n'\
          'Wins for B: {2} ({4:0.1%})\n'.format(n, winsA, winsB, winsA/n, winsB/n))

if __name__ == '__main__':
    main()
