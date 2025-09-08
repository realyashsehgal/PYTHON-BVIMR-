#Q40. Write a python code to demonstrate try, except, else and finally.
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Division successful. Result is {result}")
finally:
    print("Execution completed.")