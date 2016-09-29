# Exam Score
# exam.py

def main():
    # Introduction
    print('The program prints a grade of a score from student.')
    # Put everything in a try/except
    try:
        # Get a score input
        score = int(input('Enter a score: '))
        # Create a decision tree
        if score < 60:
            print('F')
        elif score < 70:
            print('D')
        elif score < 80:
            print('C')
        elif score < 90:
            print('B')
        elif score <= 100:
            print('A')
        else:
            print('Not a real one.')
            
    except:
        print('Something is wrong.')

if __name__ == '__main__':
    main()
