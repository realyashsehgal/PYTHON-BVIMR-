from Signature_folder.Signature import sign

def greet(name):
    """This function greets the person whose name is passed as a parameter."""
    print("Hello,", name + "!")

greet("Yash")

print("\nFunction Description:")
print(greet.__doc__)

sign()
