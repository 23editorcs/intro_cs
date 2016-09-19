# Calculator
# calculator.py

def main():
    # Instruction
    print('The Calculator program.')
    # Get the number of times to calculate
    n = eval(input('How many times do you want to calculate? '))
    # Calculator
    for i in range(n):
        output = eval(input('Type your fomular: '))
        print(output)
    # Rule them all

main()
