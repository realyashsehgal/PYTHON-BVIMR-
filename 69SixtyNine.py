#Write python code to demonstrate function with multiple returns.
from Signature_folder.Signature import sign

# function with multiple return values
def calculate(a, b):
    sum_ = a + b
    diff = a - b
    prod = a * b
    return sum_, diff, prod

# calling the function
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

s, d, p = calculate(x, y)

print("Sum:", s)
print("Difference:", d)
print("Product:", p)

sign()

