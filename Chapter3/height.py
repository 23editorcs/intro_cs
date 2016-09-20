# Oh Height Ladder
# height.py
import math

def main():
    # Instruction
    print('The program calculates the height of ladder with the angle.')
    # Get the Height of the house, the angle
    height = eval(input('How height of the house? '))
    angle = eval(input('What is the angle? '))
    # Convert the angle to radian
    angle = math.pi / 180 * angle 
    # Calculate the height of ladder
    ladder = height / math.sin(angle)
    # Rule them all
    print('The height of ladder is', ladder)

main()
