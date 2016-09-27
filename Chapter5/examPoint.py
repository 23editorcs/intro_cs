# 100-Point Exam
# examPoint.py

# Without using if, how to seperate the score from 0-100
# Lookup table?
# If a score < 60 = F => score - 60 < 0 = F
# A score // 10 = 0-10 values
# A score // 10 - 6 <= 4, how to control < 60 value
# A Lookup Table = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']

def main():
    # Introduction
    print('The program gets a score from 0-100 and returns a grade.')
    # Create a lookup table
    grades = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']
    # Get a score input
    score = eval(input('Enter the score from 0-100: '))
    # Convert to index to lookup
    index = score // 10
    # Rule them all
    print('Your grade is {0}.'.format(grades[index]))

main()
                
