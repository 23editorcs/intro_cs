# Calculate Hydrocarbon weight
# hydrocarbon.py

def main():
    # Instruction
    print('The program calculates the hydrocarbon weight.')
    # Get the number of molecular
    hydro = eval(input('How many Hydro? '))
    carbon = eval(input('How many Carbon? '))
    oxy = eval(input('How many Oxy? '))
    # Calculate the weight
    mole = (hydro * 1.0079) + (carbon * 12.011) + (oxy * 15.9994)
    # Rule them all
    print('Your molecular is: {0:.5f} grams'.format(mole))

main()
