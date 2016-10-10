# poker.py
# Poker Game with Dice

from graphics import *
from random import randrange
from button import Button
from dieview import DieView

class PokerApp:

    def __init__(self, interface, filename):
        self.dice = Dice()
        self.money = 100
        self.interface = interface
        self.filename = filename


    def run(self):
        # Draw the splash creen with High Scores table
        self.highScore()
        self.interface.splash(self.names, self.scores)
        # Run the game if player wants
        while self.money >= 10 and self.interface.wantToPlay():
            self.playRound()
        # After player finishs. check the score
        self.checkScore()
        # Close the game after check score
        self.interface.close()

    def playRound(self):
        self.money -= 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money += score
        self.interface.setMoney(self.money)

    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll += 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()
                
    def highScore(self):
        infile = open(self.filename, 'r')
        self.names, self.scores = [], []
        for line in infile:
            name = line.split()[0]
            score = int(line.split()[1])
            self.names.append(name)
            self.scores.append(score)
        infile.close()

    def checkScore(self):
        for i in range(len(self.scores)):
            if self.money >= self.scores[i]:
                self.scores.insert(i, self.money)
                name = self.interface.inputName()
                self.names.insert(i, name)
                break
        outfile = open(self.filename, 'w')
        
        for i in range(len(self.names)):
            print('{0} {1}'.format(self.names[i], self.scores[i]), file=outfile)
        outfile.close()

class Dice:

    def __init__(self):
        self.dice = [0] * 5
        self.rollAll()

    def roll(self, which):
        for pos in which:
            self.dice[pos] = randrange(1,7)

    def rollAll(self):
        self.roll(range(5))

    def values(self):
        return self.dice[:]

    def score(self):
        # Create the counts list
        counts = [0] * 7
        for value in self.dice:
            counts[value] += 1
            
        # Score the hand
        if 5 in counts: return 'Five of a Kind', 30
        elif 4 in counts: return 'Four of a Kind', 15
        elif 3 in counts and 2 in counts: return 'Full House', 12
        elif 3 in counts: return 'Three of a Kind', 8
        elif not (2 in counts) and (counts[1] == 0 or counts[6] == 0):
            return 'Straight', 20
        elif counts.count(2) == 2: return 'Pair', 5
        else: return 'Garbage', 0

class GraphicsInterface:

    def __init__(self):
        self.win = GraphWin('Poker Dice', 600, 400)
        self.win.setBackground('green2')
        self.buttons = []



    def splash(self, names, scores):
        # Create a splash screen before playing.
        self.splash = []
        play = Button(self.win, Point(200, 350), 150, 40, 'Play')
        play.activate()
        self.splash.append(play)
        quits = Button(self.win, Point(400, 350), 150, 40, 'Exit')
        quits.activate()
        self.splash.append(quits)
        self.drawHighScores(names, scores)
        self.toPlay()
        
    def drawHighScores(self, names, scores):
        rect = Rectangle(Point(200, 300), Point(400, 50))
        rect.setFill('white')
        rect.draw(self.win)
        self.splash.append(rect)
        header = Text(Point(300, 70), 'High Scores of Poker Dice')
        header.setStyle('bold')
        self.splash.append(header)
        header.draw(self.win)
        for i in range(10):
            text = Text(Point(300, 100 + i * 20), '{2:0>2}. {0:<8}\t{1:^4}'\
                        .format(names[i].capitalize(), scores[i], i + 1))
            self.splash.append(text)
            text.draw(self.win)
        
    def toPlay(self):
        p = self.win.getMouse()
        while True:
            if self.splash[0].clicked(p):
                for i in self.splash:
                    i.undraw()
                self.drawInterface()
                break
            elif self.splash[1].clicked(p):
                self.win.close()
                break
            p = self.win.getMouse()

    def drawInterface(self):
        # Draw the main interface 
        banner = Text(Point(300,30), 'Python Poker Parlor')
        banner.setSize(24)
        banner.setFill('yellow2')
        banner.setStyle('bold')
        banner.draw(self.win)
        self.msg = Text(Point(300, 380), 'Welcome to the Dice Poker')
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(Point(300,100), 75)
        self.addDiceButtons(Point(300,170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, 'Roll Dice')
        self.buttons.append(b)
        b = Button(self.win, Point(300,280), 150, 40, 'Score')
        self.buttons.append(b)
        b = Button(self.win, Point(570,375), 40, 40, 'Quit')
        self.buttons.append(b)
        self.getHelp = Button(self.win, Point(30, 375), 40, 40, 'Help')
        self.getHelp.activate()
        self.money = Text(Point(300,325), '$100')
        self.money.setSize(18)
        self.money.draw(self.win)

    def inputName(self):
        win2 = GraphWin('Enter Your name plese: ', 200, 200)
        entry = Entry(Point(100, 100), 20)
        label = Text(Point(100, 50), 'You get a high score. Well Done!')
        label.draw(win2)
        enter = Button(win2, Point(100,150), 50, 50, 'Enter')
        enter.activate()
        entry.draw(win2)
        while True:
            p = win2.getMouse()
            if enter.clicked(p) and entry.getText() != '':
                win2.close()
                return entry.getText()
            

    def createDice(self, center, size):
        center.move(-3*size, 0)
        self.dice = []
        for i in range(5):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size, 0)
        print(self.dice)

    def addDiceButtons(self, center, width, height):
        center.move(-3*width, 0)
        for i in range(1,6):
            label = 'Die {}'.format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)

    def setMoney(self, amt):
        # Change the text of money
        self.money.setText('${}'.format(amt))

    def showResult(self, msg, score):
        # Change the text of message
        if score > 0:
            text = '{0}! You win ${1}.'.format(msg, score)
        else:
            text = 'You rolled {}'.format(msg)
        self.msg.setText(text)

    def setDice(self, values):
        # Update the values of 5 interface dice with values from model
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = self.choose(['Roll Dice', 'Quit'])
        self.msg.setText('')
        return ans == 'Roll Dice'

    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            self.clickHelp(p)
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()     # function exit here

    def chooseDice(self):
        # choices is a list of indexes of the selected dice
        choices = []        # no dice chosen yet
        while True:
            # wait for user to click a valid button
            b = self.choose(['Die 1', 'Die 2', 'Die 3', 'Die 4', 'Die 5',
                             'Roll Dice', 'Score', 'Help'])

            if b[0] == 'D':             # User clicked a die button
                i = eval(b[4]) - 1      # Translate label to die index
                if i in choices:        # Currently selected, unselect it
                    choices.remove(i)
                    self.dice[i].changeColor('black')
                else:
                    choices.append(i)
                    self.dice[i].changeColor('gray')
            else:                       # User clicked Roll or Score
                for d in self.dice:     # Revert apprearance of all dice
                    d.changeColor('black')
                if b == 'Score':        # Score clicked, ignore choices
                    return []
                elif choices != []:     # Don't accept Roll unless some
                    return choices      #   dice are actualy selected

    def clickHelp(self, p):
        if self.getHelp.clicked(p):
            win1 = GraphWin('Poker Introduction', 300, 300)
            text = Text(Point(150,100),
                        'This is an introduction of Poker Dice\n'\
                        'You could have known it before\n'\
                        'But it is good to remind you again\n'\
                        '\n\n'\
                        '   Hands of Dice       Pay (scores)\n'\
                        'Two Pairs              = 5\n'\
                        'Three of a Kind        = 8\n'\
                        'Full House             = 12\n'\
                        'Four of a Kind         = 15\n'\
                        'Straight (1–5 or 2–6)  = 20\n'\
                        'Five of a Kind         = 30.')
            text._reconfig('justify', 'left')
            text.draw(win1)
    def close(self):
        self.win.close()
                    
        
        
class TextInterface:

    def __init__(self):
        print('Welcome to video player.')

    def setMoney(self, amt):
        print('Your currently have ${}'.format(amt))

    def setDice(self, values):
        print('Dice:', values)

    def wantToPlay(self):
        ans = input('Do you wist to try your luck? ')
        return ans[0] in 'Yy'

    def close(self):
        print('\nThanks for playing!')

    def showResult(self, msg, score):
        print('{0}. You win ${1}.'.format(msg, score))

    def chooseDice(self):
        return eval(input('Enter list of which to change ([ ] to stop) '))

inter = GraphicsInterface()
app = PokerApp(inter, 'highscores')
app.run()


    
        
