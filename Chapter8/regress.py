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

def main():
    # Introduction
    print('The program draws a regression line with user\'s clicks.')
    # Draw a graphic window
    win = GraphWin('Regression Line', 400, 400)
    win.setCoords(0, 0, 100, 100)
    win.setBackground('white')
    done = Text(Point(5, 5), 'Done')
    button = Rectangle(Point(1,2), Point(9,8))
    button.setOutline('red')
    button.setWidth(2)
    button.draw(win)
    done.draw(win)
    x, y = 50, 50
    sumx, sumy, sumx2, sumxy, n = 0, 0, 0, 0, 0
    while not (x < 9 and y < 8):
        p = win.getMouse()
        n += 1
        x, y = p.getX(), p.getY()
        sumx += x
        sumy += y
        sumx2 += x ** 2
        sumxy += x * y
        p.draw(win)
    meanx = sumx / n
    meany = sumy / n
    m = (sumxy - n * meanx * meany) / (sumx2 - n * (meanx ** 2))
    y1 = meany + m * (0 - meanx)
    y2 = meany + m * (100 - meanx)
    Line(Point(0, y1), Point(100, y2)).draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
