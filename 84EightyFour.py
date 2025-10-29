# List and demonstrate various standard library module of python.
from Signature_folder.Signature import sign
import math, random, datetime, os, sys, json, statistics

# math
print("Square root:", math.sqrt(16))

# random
print("Random number:", random.randint(1, 10))

# datetime
print("Today:", datetime.date.today())

# os
print("Working dir:", os.getcwd())

# sys
print("Python version:", sys.version.split()[0])

# json
person = {"name": "Yash", "age": 21}
print("JSON:", json.dumps(person))

# statistics
data = [10, 20, 30, 40]
print("Mean:", statistics.mean(data))

sign()
