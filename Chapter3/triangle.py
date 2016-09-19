# Triangle Area
# triangle.py
import math

def main():
    # Instruction
    print('The program calculates the area triangle with given length.')
    # Get 3 length of lines
    a, b, c = eval(input('Enter the length of 3 lines:(separate by commas) '))
    # Calculate the area
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    # Rule them all
    print('The area is {0:.2f}.'.format(area))

main()
