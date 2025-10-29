#Wap in python to check whether the string is palindrome or not.
from Signature_folder.Signature import sign

# program to check whether a string is palindrome or not
text = input("Enter a string: ")

# reversing the string manually
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

if text == reversed_text:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

sign()
