#Write python code to print Fibonacci series upto given input number using both simple function (non-recursive) and recursive function.
from Signature_folder.Signature import sign

# simple (non-recursive) function
def fibonacci_non_recursive(n):
    a, b = 0, 1
    print("Fibonacci Series (Non-Recursive):", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# recursive function
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# taking input
num = int(input("Enter number of terms: "))

# calling both functions
fibonacci_non_recursive(num)

print("Fibonacci Series (Recursive):", end=" ")
for i in range(num):
    print(fibonacci_recursive(i), end=" ")

print()

sign()

