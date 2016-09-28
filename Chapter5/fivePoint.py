# 5-Point Quizzes
# fivePoint.py

def main():
    # Introduction
    print('The program gets a score and returns a grade.') 
    # Get the file name of scores
    fileName = input('File name: ')
    # Open the file
    infile = open(fileName, 'r')
    # Create a list to be a lookup table
    grades = ['E', 'D', 'C', 'B', 'A']
    # Get the score line by line
    for i in infile:
        score = eval(i)
        # Return a grade
        print('Your grade is {0}.'.format(grades[score-1]))
    # Rule them all
    infile.close()

main()
