# Pizza per Inch calculation
# pizza.py
import math

def main():
    # Instruction
    print('The program calculates price per inch of a pizza.')
    # Get the price and inch of pizza
    price = eval(input('How much is your pizza?($) '))
    inch = eval(input('How big is it?(inch) '))
    # Calculate price per inch
    # Calculate the area of pizza
    a = math.pi * inch ** 2
    pricePerInch = price / a
    # Rule them all
    print('You pizza price per inch is', str(round(pricePerInch, 2)) + '/inch^2')

main()
