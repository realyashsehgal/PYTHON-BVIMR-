# creating a generator
def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i

# using the generator inside a loop
for num in even_numbers(10):
    print(num)
