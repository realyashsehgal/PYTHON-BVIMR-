try:
    x = int("abc")
except ValueError:
    print("ValueError occurred")
finally:
    print("This always runs")
from Signature_folder.Signature import sign
sign()