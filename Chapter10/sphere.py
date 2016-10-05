# sphere.py
# Sphere Class

from math import pi

class Sphere:
    """ A Sphere returns area and volume with getArea and getVolume methods.
        Returns the radius with getRadius method."""

    def __init__(self, radius):
        self.radius = radius
        self.area = pi * radius ** 2
        self.volume = 4/3 * pi * radius ** 3

    def getRadius(self):
        return self.radius

    def getArea(self):
        return self.area

    def getVolume(self):
        return self.volume
