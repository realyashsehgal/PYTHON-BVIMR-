from Signature_folder.Signature import sign
a, b, c = 1, 2, 3
temp = a
a = b
b = c
c = temp
print("After swap using temp variable:", a, b, c)

a, b, c = 1, 2, 3
a, b, c = b, c, a
print("After swap:", a, b, c)

a, b, c = 1, 2, 3
a = a + b + c
b = a - (b + c)
c = a - (b + c)
a = a - (b + c)
print("After swap using arithmetic operations:", a, b, c)

sign()