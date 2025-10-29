#Write python code to create a custom module (user-defined module).
# mymodule.py

def greet(name):
    return f"Hello, {name}! Welcome to Python modules."

def add(a, b):
    return a + b

from Signature_folder.Signature import sign
import mymodule

# Using functions from our custom module
print(mymodule.greet("Yash"))
print("Addition:", mymodule.add(10, 5))

sign()
