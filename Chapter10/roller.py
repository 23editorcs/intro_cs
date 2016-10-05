# roller.py
# Roller Roller Roller

from graphics import *
from random import randrange
from dieview import DieView
from cbutton import CButton

def main():

    # create the application window
    win = GraphWin('Roller', 500, 500)
    win.setBackground('green2')
    win.setCoords(0, 0, 10, 10)

    # draw the interface widgets
    die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    rollButton = CButton(win, Point(5, 4.5), 1, 'Roll Dice')
    rollButton.activate()
    quitButton = CButton(win, Point(5, 1), 1, 'Quit')

    # event loop
    p = win.getMouse()
    while not quitButton.clicked(p):
        if rollButton.clicked(p):
            die1.addColor(color_rgb(randrange(1,256), randrange(1,256), randrange(1,256)))
            die1.setValue(randrange(1,7))
            die2.setValue(randrange(1,7))
            quitButton.activate()
        p = win.getMouse()

    # Close the window
    win.close()

if __name__ == '__main__':
    main()
        

    
    
    


