#Write python code to demonstrate method overloading and method overriding.
from Signature_folder.Signature import sign

# -------- METHOD OVERLOADING --------
# (Python doesn’t support true overloading, so we simulate it using default arguments)
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

# -------- METHOD OVERRIDING --------
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

sign()
