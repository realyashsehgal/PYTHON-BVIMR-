#Write python code to demonstrate function with default parameter.
from Signature_folder.Signature import sign

# function with default parameter
def greet(name="Guest"):
    print("Hello,", name + "! Welcome back.")

# calling the function
greet("Yash")
greet()  # uses default value

sign()
