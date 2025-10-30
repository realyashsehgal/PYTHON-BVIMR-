from Signature_folder.Signature import sign

text = input("Enter a string: ")

count = 0
for char in text:
    count += 1

print("Length of the string:", count)

sign()
