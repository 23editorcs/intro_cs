# cannonball.py
# Simulation The Flying CannonBall

'''
    Input the simulation parameter: angle, velocity, height, interval
    Calculate the inital position of the cannonball: xpos, ypos
    Calculate the inital velocities of the cannonball: xvel, yvel
    While the cannonball is still flying:
     update the values of xpos, ypos, and yvel for interval seconds
      further into the flight
    Output the distance traveled as xpos
'''

from math import cos, sin, radians

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print('\nThe distrance traveled: %0.1f meters.' % (cball.getMaxY()))

def getInputs():
    angle = float(input('What is the angle of the launch: '))
    vel = float(input('What is the initial velocity: '))
    h0 = float(input('What is the height: ' ))
    time = float(input('Enter the time interval between calculations: '))
    return angle, vel, h0, time
    
class Projectile:

    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        # No more use so do not need create instance variable
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
        maxYPos = (self.yvel / 9.8) * self.yvel / 2.0
        self.maxHeight = height + maxYPos

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos
    
    def getMaxY(self): 
        return self.maxHeight 
        
    def update(self, time):
        self.xpos = self.xpos + self.xvel * time
        yvel1 = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

if __name__ == '__main__':
    main()
        
