#Write python code to demonstrate docstring for a function
from Signature_folder.Signature import sign

# function with docstring
def greet(name):
    """This function greets the person whose name is passed as a parameter."""
    print("Hello,", name + "!")

# calling the function
greet("Yash")

# accessing the docstring
print("\nFunction Description:")
print(greet.__doc__)

sign()
