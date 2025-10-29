#Write python code to demonstrate function with return.
from Signature_folder.Signature import sign

# function with return value
def add(a, b):
    result = a + b
    return result

# calling the function and printing result
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum is:", add(x, y))

sign()
