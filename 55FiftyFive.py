def gen_numbers():
    for i in range(1, 4):
        yield i

def square_numbers(numbers):
    for n in numbers:
        yield n * n

for value in square_numbers(gen_numbers()):
    print(value)

from Signature_folder.Signature import sign
sign()