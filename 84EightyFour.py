from Signature_folder.Signature import sign
import math, random, datetime, os, sys, json, statistics

print("Square root:", math.sqrt(16))

print("Random number:", random.randint(1, 10))

print("Today:", datetime.date.today())

print("Working dir:", os.getcwd())

print("Python version:", sys.version.split()[0])

person = {"name": "Yash", "age": 21}
print("JSON:", json.dumps(person))

data = [10, 20, 30, 40]
print("Mean:", statistics.mean(data))

sign()
