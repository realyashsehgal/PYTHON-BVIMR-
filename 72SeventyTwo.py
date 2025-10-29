#Wap in python to reverse a string without using predefined functions.
from Signature_folder.Signature import sign

# program to reverse a string without using predefined functions
text = input("Enter a string: ")

reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

print("Reversed string:", reversed_text)

sign()
