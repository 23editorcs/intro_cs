# Convert Temperature
# convert.py

def main():
    # Instruction
    print('The program converts the Fahrenheit to Celsius.')
    # Loop 5 times
    for i in range(5):
        # Get the Fahrenheit temperature from user
        fah = eval(input('Please enter the temperature (Fahrenheit): '))
        # Convert it to Celsius
        cel = 5/9 * (fah - 32)
        # Rule them all
        print('Your Celsius temperature is:', round(cel,2))

main()
