#Write a python code to chain generators.
# first generator
def gen_numbers():
    for i in range(1, 4):
        yield i

# second generator that uses the first
def square_numbers(numbers):
    for n in numbers:
        yield n * n

# chaining generators
for value in square_numbers(gen_numbers()):
    print(value)
