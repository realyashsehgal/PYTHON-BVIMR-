#Write a python code to demonstrate global variables with nested function.
from Signature_folder.Signature import sign

# global variable
count = 0

def outer_function():
    global count
    count += 1
    print("Count in outer_function:", count)

    def inner_function():
        global count
        count += 1
        print("Count in inner_function:", count)

    inner_function()

# calling the outer function
outer_function()
print("Count outside function:", count)

sign()
