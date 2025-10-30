from Signature_folder.Signature import sign
def is_perfect(n):
    return n == sum(i for i in range(1, n // 2 + 1) if n % i == 0)

perfect_numbers = [i for i in range(1, 2026) if is_perfect(i)]
for num in perfect_numbers:
    print(num)
print("Total count:", len(perfect_numbers))
sign()