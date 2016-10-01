# gcd.py
# Greatest Common Divisor

def main():
    # Introduction
    print('The program finds a greatest common divisor of 2 numbers.')
    # Get two numbers input
    n, m = eval(input('Enter two numbers (separate by comma): '))
    while m != 0:
        n, m = m, n % m
    print('Your greatest common divisor is {0}.'.format(n))

if __name__ == '__main__':
    main()
