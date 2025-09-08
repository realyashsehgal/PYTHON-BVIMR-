#Q39. Write a python code to demonstrate try and except and finally.
try:
    x = int("abc")
except ValueError:
    print("ValueError occurred")
finally:
    print("This always runs")