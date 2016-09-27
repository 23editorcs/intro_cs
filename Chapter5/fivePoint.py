# 5-Point Quizzes
# fivePoint.py

def main():
    # Introduction
    print('The program gets a score and returns a grade.') 
    # Get a score of quizz
    score = eval(input('Enter your score: '))
    # Return a grade
    # Create a list to be a lookup table
    grades = ['F', 'E', 'D', 'C', 'B', 'A']
    print('Your grade is {0}.'.format(grades[score]))
    # Rule them all

main()
