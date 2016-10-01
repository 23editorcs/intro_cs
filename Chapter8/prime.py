# prime.py
# Define prime number
import math

def main():
    # Introduction
    print('The program defines a number is prime or not.')
    # Get the input
    x = int(input('Enter a number: '))
    # Loop from 3 to sqrt(x) to define a number evenly divides x
    i = 2
    while i < math.sqrt(x):
        if x % i == 0: return False
        i += 1
    print('Your number is prime.')

if __name__ == '__main__':
    main()
