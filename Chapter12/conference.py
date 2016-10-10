# conference.py
# Chapter 12, exercise 3

def main():
    print('Welcome to Conference')
    filename = input('Enter a file name of attendee: ')
    theCon = Conference(filename)
    while True:
        order = input('Enter an order (add, del, list, listA, listS: ')
        if order == 'add':
            addMethod()
        elif order == 'del':
            delMethod()
        elif order == 'list':
            listMethod()
        elif order == 'listA':
            listAllMethod()
        elif order == 'listS':
            listStateMethod()
        else:
            break
    
        
class Conference:
    """ A Conference object that holds all information of a conference"""
    def __init__(self, filename):
        # List of Attendee objecs
        self.attendees = []
        # File to read the attendees object
        self.filename = filename
        # Open the file
        infile = open(self.filename, 'r')
        # Loop through line to make an Attendee object
        for line in infile:
            # A line inlucde Name, Email, Company, State separate by tabs
            name, email, com, state = map(str, line.split('\t'))
            # Create an Attendee object
            attendee = Attendee(name, email, com, state)
            # Add an Attendee to Conference list
            self.attendees.append(attendee)
        infile.close()

    def addAttendee(self, name, email, com, state):
        attendee = Attendee(name, email, com, state)
        self.attendees.append(attendee)

    def delAttendee(self, name):
        for att in self.attendees:
            if name == att.getName():
                self.attendees.remove(att)

    def listAttendee(self, name):
        for att in self.attendees:
            if name == att.getName():
                return att

    def listAll(self):
        return self.attendees

    def listAllState(self, state):
        stateList = []
        for att in self.attendees:
            if state == att.getState():
                stateList.append(att)
        return stateList        
        
class Attendee:
    """ Create an Attendee profile"""
    def __init__(self, name, email, com, state):
        self.name = name
        self.email = email
        self.com = com
        self.state = state

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getCom(self):
        return self.com

    def getState(self):
        return self.state


    
        

