# Lightning Distance
# lightning.py

def main():
    # Instruction
    print('The program calculates the distance of a lightning'\
          'in kilometers not miles. I hate mile.')
    # Get the time elapsed between the image and sound
    time = eval(input('How long is the time elapsed between flash'\
                      'and sound?(in second) '))
    # Calculate the distance in kilometer
    # lightning speed = 1100 ft/sec, 1 mile = 5280 ft, 1 km = 0.62 mile
    distance = time * 1100 / 5280 / 0.62
    # Rule them all
    print('The distance of lightniing is {0:.2f} kilometer'.format(distance))

main()
