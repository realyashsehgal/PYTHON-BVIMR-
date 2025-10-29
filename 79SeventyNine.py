#Write python code to demonstrate decorator using functiontool.wraps.
from Signature_folder.Signature import sign
from functools import wraps

# Decorator using functools.wraps
def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, Keyword Arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@debug
def add(a, b):
    """This function adds two numbers."""
    return a + b

# Function call
print(add(10, 5))
print(f"Function name: {add.__name__}")
print(f"Docstring: {add.__doc__}")

sign()
