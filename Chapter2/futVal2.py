# Future Value with Compounding Periods
# futVal2.py

def main():
    # Instruction
    print('The program calculates Future Value with Compound Periods.')
    # Get user's input: principal, annualized interest rate,
    # years, compounding periods
    principal = eval(input('How much do you save? '))
    apr = eval(input('How is the interest? '))
    years = eval(input('How lond do you save? '))
    periods = eval(input('How many periods in a year? '))
    # Print Header
    print('{0:^5} {1}'.format('Period', 'Your Money'))
    # Calculate Future Values
    for i in range(years * periods + 1):
        futVal = principal * (1 + apr/periods)**i
        print('{0:^5} {1:^10.2f}'.format(i, futVal))
    # Rule them all

main()
