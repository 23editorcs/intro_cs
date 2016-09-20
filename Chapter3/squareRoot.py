# Square Root program
# squareRoot.py
import math

def main():
    # Instruction
    print('The program returns your square root.')
    # Get user's number and how many times to loop
    x = eval(input('What is the number? '))
    n = eval(input('How many times to loop? '))
    # Loop through Newton's method
    guess = x / 2
    for i in range(n):
        guess = (guess + x / guess) / 2        
    # Rule them all
    print('Your square root is', guess)
    print('True square root is {0}, and the difference is {1}.'\
          .format(math.sqrt(x), math.sqrt(x) - guess))

main()
