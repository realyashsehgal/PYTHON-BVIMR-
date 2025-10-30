from Signature_folder.Signature import sign

count = 0

def outer_function():
    global count
    count += 1
    print("Count in outer_function:", count)

    def inner_function():
        global count
        count += 1
        print("Count in inner_function:", count)

    inner_function()

outer_function()
print("Count outside function:", count)

sign()
