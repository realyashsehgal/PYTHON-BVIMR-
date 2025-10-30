from Signature_folder.Signature import sign

def fibonacci_non_recursive(n):
    a, b = 0, 1
    print("Fibonacci Series (Non-Recursive):", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

num = int(input("Enter number of terms: "))

fibonacci_non_recursive(num)

print("Fibonacci Series (Recursive):", end=" ")
for i in range(num):
    print(fibonacci_recursive(i), end=" ")

print()

sign()

