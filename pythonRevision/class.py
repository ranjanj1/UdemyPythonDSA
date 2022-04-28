class Student:
    '''This is version 1.0'''
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def __str__(self):
        return 'This is student class'

    def display(self):
        print('Student Name:', self.name)
        print('Student roll:', self.roll)
        print('Student marks:', self.marks)



S = Student('test',00,45)  # creation of object of class student

print(S.name)
print(S.roll)
print(S.marks)

print(S.__doc__)

print(S)  # o/p : This is student class

S.display()

S1 = Student('aaa', 11, 45)
S2 = Student('bbb', 22, 55)
S3 = Student('ccc', 33, 65)

S1.display()
S2.display()
S3.display()
