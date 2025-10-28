#Write a python code to use iterator inside a loop.
# creating a list
fruits = ["apple", "banana", "mango"]

# getting iterator
it = iter(fruits)

# using iterator inside a loop
for fruit in it:
    print(fruit)
