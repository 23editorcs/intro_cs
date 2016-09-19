# Chaos Program

def chaos39():
    # Instruction
    print('The program runs a chaos program with 3.9 and prints 10 output.')
    # Get User's input
    x = eval(input('Enter a number: '))
    # Loop to 10
    for i in range(10):
        x = 3.9 * x * (1 - x) # Chaos formula - Logistic formula
        print(x)
    # Rule them all

def chaos20():
    # Instruction
    print('The program runs a chaos program with 2.0 and prints 10 output.')
    # Get User's input
    x = eval(input('Enter a number: '))
    # Loop to 10
    for i in range(10):
        x = 2.0 * x * (1 - x) # Chaos formula - Logistic formula
        print(x)
    # Rule them all

def chaosN():
    # Instruction
    print('The program runs a chaos program with 3.9 and prints N output.')
    # Get User's input
    n = eval(input('How many times you want to loop? '))
    x = eval(input('Enter a number: '))
    # Loop to 10
    for i in range(n):
        x = 3.9 * x * (1 - x) # Chaos formula - Logistic formula
        print(x)
    # Rule them all
             
def chaosThree():
    # Instruction
    print('The program runs a chaos program with 3.9 and prints N output.')
    print('With 3 formulas.')
    # Get User's input
    n = eval(input('How many times you want to loop? '))
    x = eval(input('Enter a number: '))
    # Print Label
    print('{0:7} {1:7} {2:7} {3:7}'.format('one','two','three', 'four'))
    # 0: width indicates numeric.
    # Loop to 10
    for i in range(n):
        x1 = 3.9 * x * (1 - x) # Chaos formula - Logistic formula
        x2 = 3.9 * (x - x * x)
        x3 = 3.9 * x - 3.9 * x * x      
        print('{0:0} {1:7f} {2:7f} {3:7f}'.format(i, x1, x2, x3))
    # Rule them all    

chaos39()
chaos20()
chaosN()
chaosThree()
             
