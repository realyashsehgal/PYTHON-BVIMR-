#Write python code to demonstrate decorator with argument.
from Signature_folder.Signature import sign

# Decorator that accepts arguments
def smart_divide(func):
    def wrapper(a, b):
        print(f"Dividing {a} by {b}")
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return
        return func(a, b)
    return wrapper

@smart_divide
def divide(a, b):
    return a / b

# Calling the decorated function
result = divide(10, 2)
print("Result:", result)

result = divide(8, 0)

sign()
