#Write python code to print factorial of a given number using simple function (without recursion).
from Signature_folder.Signature import sign

# function to calculate factorial without recursion
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# taking input
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))

sign()
