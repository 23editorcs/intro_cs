# invest.py
# Calculate how long the investment is double

'''
    Input the annualized interest rate
    Loop until the principal is double
     Increase the principal with the apr every loop
     Count every loop
    Return the Count
'''   
def main():
    # Introduction
    print('The program calculate how long it takes to double you investment'\
          'with an annualized interest.')
    # Get the initialized interest rate
    apr = float(input('Enter the annualized interest rate: '))
    # Loop until the principal is double
    prin = 1
    count = 0
    while prin < 2:
        prin= prin * (1 + apr)
        count += 1
    print('\nYour investment is double in {0} years.'.format(count))

if __name__ == '__main__':
    main()
