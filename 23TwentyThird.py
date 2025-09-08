#Q23. Write python code to demonstrate list comprehensions.
# Example: Create a list of squares from 0 to 9 using list comprehension
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# Example: Filter even numbers from a list using list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)

# Example: Convert a list of strings to uppercase using list comprehension
words = ['python', 'list', 'comprehension']
upper_words = [word.upper() for word in words]
print("Uppercase words:", upper_words)