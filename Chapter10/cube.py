# cube.py

class Cube:

    def __init__(self, a):
        self.length = a
        self.area = 6 * a * a
        self.volume = a ** 3

    def getLength(self):
        return self.length

    def getArea(self):
        return self.area

    def getVolume(self):
        return self.volume

    
