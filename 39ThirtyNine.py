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
from Signature_folder.Signature import sign
sign()