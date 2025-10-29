#Write python code to demonstrate global variable.
from Signature_folder.Signature import sign

# global variable
count = 0

def increment():
    global count
    count += 1
    print("Count inside function:", count)

# calling function multiple times
increment()
increment()
increment()

print("Count outside function:", count)

sign()