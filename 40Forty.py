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
from Signature_folder.Signature import sign
sign()