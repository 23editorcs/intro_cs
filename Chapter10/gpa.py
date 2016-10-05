# gpa.py
# Program that find a student with highest gpa

class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours

    def addGrade(self, gradePoint, credit):
        self.qpoints = self.qpoints + gradePoint
        self.hours = self.hours + credit

    def addLetterGrade(self, letter, credit):
        if letter == 'A':    self.qpoints += 4.0
        elif letter == 'A-': self.qpoints += 3.7
        elif letter == 'B+': self.qpoints += 3.3
        elif letter == 'B':  self.qpoints += 3.0
        elif letter == 'B-': self.qpoints += 2.7
        elif letter == 'C+': self.qpoints += 2.3
        elif letter == 'C':  self.qpoints += 2.0
        self.hours += credit
            
    
def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # Returns a corresponding Student object
    name, hours, qpoints = infoStr.split('\t')
    return Student(name, hours, qpoints)

def main():
    # Open the input file for reading
    s = makeStudent('Quy\t0\t0')
    letter = input('Enter a grade point: ')
    credit = float(input('Enter a credit of the course: '))
    s.addLetterGrade(letter, credit)
    print(s.getHours(), s.gpa())
    


if __name__ == '__main__':
    main()

