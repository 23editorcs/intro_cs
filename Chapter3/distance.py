# Distance Calculation
# distance.py

import math

def main():
    # Instruction
    print('The program calculates the distance between two points.')
    # Get two points
    x1, y1, x2, y2 = eval(input('Enter two points x1, y1, x2, y2:'\
                                '(separate by commas) '))
    # Calculate the distance
    distance = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    # Rule them all
    print('The distance is {0:.2f}.'.format(distance))

main()
