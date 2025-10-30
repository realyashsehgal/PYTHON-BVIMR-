

class MathOperation:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return a

m = MathOperation()
print("Add two numbers:", m.add(10, 20))
print("Add three numbers:", m.add(10, 20, 30))

class Parent:
    def show(self):
        print("This is the parent class method.")

class Child(Parent):
    def show(self):
        print("This is the child class method (overridden).")

p = Parent()
c = Child()

p.show()
c.show()
from Signature_folder.Signature import sign
sign()
