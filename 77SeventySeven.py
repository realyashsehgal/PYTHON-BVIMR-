from Signature_folder.Signature import sign

def greet_decorator(func):
    def wrapper():
        print(" Welcome to the program")
        func()
        print(" Execution completed successfully!")
    return wrapper

@greet_decorator
def say_hello():
    print("Hello, Yash!")

say_hello()

sign()
