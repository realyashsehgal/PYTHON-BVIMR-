squares = [x**2 for x in range(10)]
print("Squares:", squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)

words = ['python', 'list', 'comprehension']
upper_words = [word.upper() for word in words]
print("Uppercase words:", upper_words)

from Signature_folder.Signature import sign
sign()