#. Wap in python to calculate the length of a string without using built-in Len() function. '
from Signature_folder.Signature import sign

# program to calculate length of a string without using len()
text = input("Enter a string: ")

count = 0
for char in text:
    count += 1

print("Length of the string:", count)

sign()
