# evenPrime.py
# An even number is sum of two prime numbers

'''
 Get an input number
 Check it even
  if not, quit
 Loop i from 1 to sqrt(n)
  Check if i is a prime
   if yes, get j = n - i
   Check if j is a prime
    if yes, break the loop, return i,j
'''

import math

def main():
    # Introduction
    print('The program finds the sum of two prime numbers that equals to even number.')

    # Get the even number input
    n = int(input('Enter a number: '))
    if n % 2 != 0:
        print('Your number is not even.')
        return False
    i = 1
    while i <= math.sqrt(n):
        if isPrime(i):
            j = n - i
            if isPrime(j):
                print('Your sum of two prime number is {0} and {1}.'.format(i, j))
                return True
        i += 1
    print('Something is wrong')
def isPrime(x):
    i = 2
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    main()
