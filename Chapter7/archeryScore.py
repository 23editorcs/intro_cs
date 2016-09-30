# Archery Scorer
# archeryScore.py

from graphics import *
import math

def main():
    # Introduction
    print('The program draws a Archery and let user shots 5 times.' \
          ' Prints out the scores and total score.')
    # Draw a Graphic Window
    win = GraphWin('The Archery Game', 400, 400)
    # Draw 5-band archery
    archeryDrawer(win)
    # Shotting time
    archeryShot(win, 5)
    # End the game
    win.getMouse()
    win.close()

def archeryDrawer(win):
    bands = ['white', 'blue', 'green', 'black', 'yellow']
    radius = 200
    for i in range(len(bands)):
        color = Circle(Point(200, 200), radius - i * 40)
        color.setFill(bands[i])
        color.draw(win)

    
def archeryShot(win, times):
    total = 0
    score = 0
    label = Text(Point(200, 380), 'Your score: {0}, total: {1}.'.format(score, total))

    for i in range(times):
        p = win.getMouse()
        label.undraw()
        xp, yp = p.getX(), p.getY()
        distance = math.sqrt(xp ** 2 + yp ** 2)
        if distance <= 40:
            score = 9
        elif distance <= 80:
            score = 7
        elif distance <= 120:
            score = 5
        elif distance <= 160:
            score = 3
        else:
            score = 1
        total = total + score
        label.setText('Your score: {0}, total: {1}.'.format(score, total))
        label.draw(win)
        
if __name__ == '__main__':
    main()
