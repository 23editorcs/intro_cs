# Future Value
# futVal.py

def main():
    # Instruction
    print('The program calculates your future value of an investment.')
    # Get user's input: principal, annualized interest rate, years
    principal = eval(input('How much is your saving: '))
    apr = eval(input('What is the bank\'s interest: '))
    years = eval(input('How long do you save: '))
    # Calculate future value
    principal = principal * (1 + apr) ** years
    # Rule them all
    print('Your future value after', years, 'years is:'\
          , round(principal,2), '$')

main()
