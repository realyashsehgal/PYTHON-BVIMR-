from Signature_folder.Signature import sign

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)

s1 = Student("Yash", 21)
s2 = Student("Aarav", 22)

s1.display()
s2.display()

sign()
