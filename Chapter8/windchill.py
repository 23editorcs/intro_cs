# The WindChill Index
# windchill.py

# Print the header of the table with -20 to 60F, seperate by 6 spaces
# Print every line starts with the wind speed, then the value, seperate with
# 6 spaces

def main():
    # Introduction
    print('The program print the windchill index from -20 to 60F and 0 to 50 mph of wind.')
    # Print the header
    header = ['Speed/Temp', -20, -10, 0, 10, 20, 30, 40, 50, 60]
    for i in header:
        print('{0:6}'.format(i), end=' ')
    # Nested-Loop temperature inside wind speed
    print('\n')
    for v in range(0, 51, 5):
        print('{0:^10}'.format(v), end=' ')
        for t in range(-20, 61, 10):
            w = 35.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)
            print('{0:6}'.format(round(w,2)), end=' ')
        print('\n')
            
if __name__ == '__main__':
    main()
