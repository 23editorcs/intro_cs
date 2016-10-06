# tracker.py

from graphics import *

class Tracker:

    def __init__(self, win, objToTrack):
        """ Win is a graph win and objToTrack is an object whose
            position is to be shown in the window. objToTrack is an object
            that has getX() and getY() methods that report its current pos"""
        self.win = win
        self.x = objToTrack.getX()
        self.y = objToTrack.getY()
        self.cir = Circle(Point(self.x, self.y), 5)
        self.cir.draw(win)
        
    def update(self, objToTrack):
        self.cir.undraw()
        dx = objToTrack.getX() - self.x
        dy = objToTrack.getY() - self.y
        self.x = objToTrack.getX()
        self.y = objToTrack.getY()
        self.cir.move(dx, dy)
        self.cir.draw(self.win)

    def __str__(self):
        return str(self.y)
        
        
