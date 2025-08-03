from Signature_folder.Signature import sign
#Writing a program to demonstrate INDENTATION
def checkAge():
    age = int(input('Please enter your age'))
    if age >=18:
        print("You can vote")
#Here in the above snippet the age and i statement comes under checkAge function and print statment comes under if statement
for i in range(0,5):
    for j in range(i,5):
        print("Outer loop ", i, " Inner loop ",j)
checkAge()
sign()