from Signature_folder.Signature import sign

def calculate(a, b):
    sum_ = a + b
    diff = a - b
    prod = a * b
    return sum_, diff, prod

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

s, d, p = calculate(x, y)

print("Sum:", s)
print("Difference:", d)
print("Product:", p)

sign()

