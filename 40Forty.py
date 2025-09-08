#Q41. Write a python code to read content of a file using try, except and finally.
try:
    with open('sample.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File read operation completed.")