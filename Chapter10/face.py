# face.py

from graphics import *

class Face:

    def __init__(self, win, center, size):
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = Circle(center, size)
        self.head.draw(win)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(win)
        self.rightEye.draw(win)
        p1 = center.clone()
        p1.move(-mouthSize / 2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize / 2, mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(win)

    def smile(self):
        self.mouth.undraw()
        p1.move(


def main():
    win = GraphWin('Face',500,500)
    f = Face(win, Point(250,250), 100)

main()
