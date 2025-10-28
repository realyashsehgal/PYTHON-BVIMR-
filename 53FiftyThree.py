# Write a python code to create a simple generator.
# creating a simple generator
def count_upto(n):
    for i in range(1, n + 1):
        yield i

# using the generator
for num in count_upto(5):
    print(num)
