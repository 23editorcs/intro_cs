# threeButtonMonte.py
# Three Button Monte

from graphics import *
from button import *
from random import randrange

def main():
    """The program simulates the "Three Button Monte" game.
    Allow user chooses one of three doors and pops out the result.
    The program draws a window with 3 doors. One of the door is special.
    User clicks one of them. If clicks to the special, print the message
    winning. Otherwise, print the message in the special one.
    """
    win = GraphWin('Three Button Monte', 400, 400)
    win.setCoords(0, 0, 100, 100)
    d2 = Button(win, Point(50, 50), 25, 60, 'Door 2')
    d1 = Button(win, Point(20, 50), 25, 60, 'Door 1')
    d3 = Button(win, Point(80, 50), 25, 60, 'Door 3')
    quitButton = Button(win, Point(80, 10), 20, 10, 'Quit')
    # Get mouse click
    wins = loses = 0
    p = win.getMouse()
    # Play multiple times
    while not quitButton.clicked(p):
    # Check the click is inside one of 3 button and right or wrong
        theDoor = chooseOneDoor(d1, d2, d3)
        message, wins, loses = checkClick(p, theDoor, wins, loses)
        label = Text(Point(50, 10), message)
        winning = Text(Point(40, 5), 'Wins: {}'.format(wins))
        losing = Text(Point(60, 5), 'Loses: {}'.format(loses))
        
        label.draw(win)
        winning.draw(win)
        losing.draw(win)
        
        p = win.getMouse()
        
        label.undraw()
        winning.undraw()
        losing.undraw()
        
    win.close()
    
def chooseOneDoor(d1, d2, d3):
    x = randrange(1, 4)   
    if x == 1:
        d1.choose()
        return d1
    elif x == 2:
        d2.choose()
        return d2
    else:
        d3.choose()
        return d3
    
def checkClick(p, theDoor, wins, loses):
    if theDoor.clicked(p):
        message = 'Right! Well Done.'
        wins += 1
    else:
        message = 'Wrong! The door is ' + theDoor.getLabel().getText()
        loses += 1
    return message, wins, loses
        


if __name__ == '__main__':
    main()
