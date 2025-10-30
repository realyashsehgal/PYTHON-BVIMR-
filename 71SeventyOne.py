from Signature_folder.Signature import sign

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Armstrong numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    order = len(str(num))
    sum_ = sum(int(digit) ** order for digit in str(num))
    if num == sum_:
        print(num)

sign()
