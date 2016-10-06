# regress.py
# Draw a regression line
'''
    Draw a graphical window
    Draw a Done Button on the left edge
    Loop until user clicks Done
     Get the mouse click
     Count the number of clicks
     Sum of x, y, x*2, x*y
    Calculate y1, y2 with x1, x2 in the left and right edge
    Draw a line with 2 points
'''
from graphics import *
from regClass import Regression
from button import Button

        
    
def main():
    # Introduction
    print('The program draws a regression line with user\'s clicks.')
    # Draw a graphic window
    win = GraphWin('Regression Line', 400, 400)
    win.setCoords(0, 0, 100, 100)
    win.setBackground('white')
    button = Button(win, Point(5,5), 8, 6, "Done")
    button.rect.setOutline('red')
    button.activate()
    r = Regression()
    p = win.getMouse()
    while not button.clicked(p):
        r.addPoint(p)
        p.draw(win)
        p = win.getMouse()
    y1 = r.predict(0)
    y2 = r.predict(100)
    Line(Point(0, y1), Point(100, y2)).draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
