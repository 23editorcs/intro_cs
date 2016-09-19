# The Slope
# slope.py

def main():
    # Instruction
    print('The program calculate the slope from two points.')
    # Get two point from user
    x1, y1, x2, y2 = eval(input('Enter two point (x1, y1) (x2, y2)'\
                                '(separate by commas): '))
    # Calculate the slope
    slope = (y2 - y1) / (x2 - x1)
    # Rule them all
    print('The slope is {0:.2f}.'.format(slope))

main()
