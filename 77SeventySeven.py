#Write python code to demonstrate decorator.
from Signature_folder.Signature import sign

# decorator function
def greet_decorator(func):
    def wrapper():
        print(" Welcome to the program")
        func()
        print(" Execution completed successfully!")
    return wrapper

# function to decorate
@greet_decorator
def say_hello():
    print("Hello, Yash!")

# calling the decorated function
say_hello()

sign()
