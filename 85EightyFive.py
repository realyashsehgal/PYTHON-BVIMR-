#Write python code to define a class create its objects and access the properties in methods of the objects.
from Signature_folder.Signature import sign

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)

# Creating objects
s1 = Student("Yash", 21)
s2 = Student("Aarav", 22)

# Accessing properties through method
s1.display()
s2.display()

sign()
