from Signature_folder.Signature import sign

count = 0

def increment():
    global count
    count += 1
    print("Count inside function:", count)

increment()
increment()
increment()

print("Count outside function:", count)

sign()