# Body Mass Index
# bmi.py

def main():
    # Introduction
    print('The program calculates BMI of a person.')
    # Put all code in a try/except
        # Get a mass in kilogram and a height in meter
    mass, height = eval(input('Enter your mass and height:'\
                                 '(seperate by comma) '))
        # Change them into pounds and inches
    mass = kiloToPound(mass)
    height = meterToInch(height)
        # Calculate the BMI
    bmi = mass * 720 / (height ** 2)
        # Create a decision tree
    if bmi < 19:
        print('Your weight is below BMI standard ({0}).'.format(bmi))
    elif bmi > 25:
        print('Your weight is above BMI standard ({0}).'.format(bmi))
    else:
        print('You are so balance ({0}).'.format(bmi))


def kiloToPound(kilo):
    pound = kilo * 2.20462
    return round(pound, 2)

def meterToInch(meter):
    inch = meter * 39.3701
    return round(inch, 2)

if __name__ == '__main__':
    main()
