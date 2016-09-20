# DRaw a some sort of face
# face.py
from graphics import *

def main():
    # Instruction
    print('The program draws a some sort of face.')
    # Draw a graphic window
    win = GraphWin('The Face', 600, 600)
    # Draw a face shape
    face = Oval(Point(400, 100), Point(100, 500))
    face.draw(win)
    # Draw eyes
    eye1 = Circle(Point(200, 200), 25)
    eye2 = Circle(Point(300, 200), 25)
    eye1.draw(win)
    eye2.draw(win)
    # Draw a nose
    nose = Rectangle(Point(235, 250), Point(265, 350))
    nose.draw(win)
    # Draw a mouth
    mouth = Oval(Point(200, 400), Point(300, 450))
    mouth.draw(win)
    # Rule them all
    win.getMouse()
    win.close()

main()
