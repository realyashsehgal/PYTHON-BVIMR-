from Signature_folder.Signature import sign

text = input("Enter a string: ")

reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

if text == reversed_text:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

sign()
