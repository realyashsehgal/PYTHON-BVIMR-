#Write python code to swap value of three variables using all possible ways.
# Method 1: Using a temporary variable
from Signature_folder.Signature import sign
a, b, c = 1, 2, 3
temp = a
a = b
b = c
c = temp
print("After swap using temp variable:", a, b, c)

# Method 2: Using tuple unpacking
a, b, c = 1, 2, 3
a, b, c = b, c, a
print("After swap:", a, b, c)

# Method 3: Using arithmetic operations
a, b, c = 1, 2, 3
a = a + b + c
b = a - (b + c)
c = a - (b + c)
a = a - (b + c)
print("After swap using arithmetic operations:", a, b, c)

sign()