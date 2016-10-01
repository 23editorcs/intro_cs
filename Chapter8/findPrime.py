# findPrime.py
# Find Prime numbers to n

'''
 Input a number n
 Loop from 3 to n (inclusive)
  Check x is a prime or not
  If x if prime, prints it out.
'''
import math

def main():
    # Introduction
    print('The program prints all prime number to n - user\'s input.')
    # Get input
    n = int(input('Enter a number: '))
    for i in range(3, n+1):
        j = 2
        prime = True
        while j <= math.sqrt(i):
            if i % j == 0:
                prime = False
                break
            j += 1
        if prime: print(i, end=', ')
    

if __name__ == '__main__':
    main()
            
