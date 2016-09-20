# Calculate pi number by handsss
# calPi.py

import math

def main():
    # Instruction
    print('The program calculates the pi from hands.')
    # Get n number
    n = eval(input('How many terms?(>0) '))
    # Calculate
    myPi = 0
    a = -1
    for i in range(1, n + 1):
        myPi = myPi + (a ** (i+1)) * (4 / (2*i -1))
    # Rule them all
    print('My Pi is', myPi)
    print('The diffenrece is', math.pi - myPi)

main()
