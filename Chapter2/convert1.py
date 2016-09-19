# Convert 1
# Print 10 - 100 degree
# convert1.py

def main():
    # Instruction
    print('The program prints the temperature from 10 to 100 Celsius and')
    print('Fahrenheit values in compare.')
    # Print the headers
    print('{0:^7} {1:^10}'.format('Celsius', 'Fahrenheit'))
    # Loop 10 times from 10 to 100
    for cel in range(10, 101, 10):
        # Print 2 kind of temperature
        fah = 9/5 * cel + 32
        print('{0:^7} {1:^10}'.format(cel, fah))
    # Rule them all

main()
