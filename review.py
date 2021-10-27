class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)
'''
Heraldo Memelli 8135627
2
100 80

 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
'''
class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, score):
        super().__init__(firstName, lastName, idNumber)
        s = map(int, score)
        self.score = sum(list(s))/len(score)
        
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def  calculate(self):
        # print("Name:", self.lastName + ",", self.firstName)
        # print("ID:", self.idNumber)
        
        if self.score >= 90 and self.score <= 100:
            return 'O'
        elif self.score >= 80 and self.score < 90:
            return 'E'
        elif self.score >= 70 and self.score < 80:
            return 'A'
        elif self.score >= 55 and self.score < 70:
            return 'P'
        elif self.score >= 40 and self.score < 55:
            return 'D'
        elif self.score < 40:
            return 'T'
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())