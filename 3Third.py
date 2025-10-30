from Signature_folder.Signature import sign
age = int(input("Please enter your age "))# Here in this snippet we are using input keyuword

print("Checking if you can drive")

if age >= 18: # Here IF is the keyword 
    print("Yes u can drive")
else: # Here ELSE is the keyword
    print("Uh huh you cannot drive")
    
for i in range (1,10):
    print(i ," Times iterated in for loop")

itr = 0
while itr <= 10 :
    print(i," Times iterated in while loop")
    itr += 1
def myFunc():
    print("This is a part of function called using myFunc()")
myFunc()
sign()