# Natural Numbers
# numbers.py

def main():
    # Instruction
    print('The program sums all the n natural numbers.')
    # Get n from user
    n = eval(input('How many numbers do you want to sum? '))
    # Sum to number n
    sums = 0
    for i in range(n + 1):
        sums += i
    # Rule them all
    print('Your sum is', sums)

def cube():
    # Instruction
    print('The program sum of the cubes all the n natural numbers.')
    # Get n from user
    n = eval(input('How many numbers do you want to sum? '))
    # Sum to number n
    sums = 0
    for i in range(n + 1):
        sums += i ** 3
    # Rule them all
    print('Your sum is', sums)

def inputNum():
    # Instruction
    print('The program sum of the inputs of all the numbers.')
    # Get n from user
    n = eval(input('How many numbers do you want to sum? '))
    # Sum to number n
    sums = 0
    for i in range(n):
        num = eval(input('What is the {0} number?'.format(i + 1)))
        sums += num
    # Rule them all
    avg = sums / n 
    print('Your sum is', sums)
    print('Your average is', float(avg))

inputNum()
