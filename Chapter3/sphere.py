# Calculate Volume and Area of Sphere
# sphere.py
import math

def main():
    # Instruction
    print('The program calculates volume and area of' \
    'a sphere with give radius.')
    # Get the radius
    r = eval(input('Give the radius(cm): '))
    # Calculate volume and sphere
    v = 4/3 * math.pi * r ** 3
    a = 4 * math.pi * r ** 2
    # Rule them all
    print('Your Volume is', v, 'and area is', a)

main()
