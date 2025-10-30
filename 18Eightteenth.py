from Signature_folder.Signature import sign
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Prime numbers:")
for num in range(start, end+1):
    if is_prime(num):
        print(num, end=' ')
print("\nPerfect numbers:")
for num in range(start, end+1):
    if is_perfect(num):
        print(num, end=' ')
print("\nArmstrong numbers:")
for num in range(start, end+1):
    if is_armstrong(num):
        print(num, end=' ')
print()
sign()