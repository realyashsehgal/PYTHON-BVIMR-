from Signature_folder.Signature import sign
def checkAge():
    age = int(input('Please enter your age'))
    if age >=18:
        print("You can vote")
for i in range(0,5):
    for j in range(i,5):
        print("Outer loop ", i, " Inner loop ",j)
checkAge()
sign()