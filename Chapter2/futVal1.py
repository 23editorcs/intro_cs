# Future Value with annual input
# futVal1.py

def main():
    # Instruction
    print('The program calculate future value of an investment with annual input.')
    # Get user's principal, annualized interest rate, years
    principal = eval(input('How much do you save every year? '))
    apr = eval(input('How much of annual interest? '))
    years = eval(input('How long do you save? '))
    # print Header
    print('{0:^4} {1}'.format('Year', 'Your Money'))
    # Calculate the future value
    futVal = 0
    for i in range(years + 1):
        futVal = futVal * (1 + apr) + principal
        print('{0:^4} {1:.2f}'.format(i, futVal))
    # Rule them all
    

main()
