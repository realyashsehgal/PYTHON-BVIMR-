#Q37. Write a python code to demonstrate try and except.
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")