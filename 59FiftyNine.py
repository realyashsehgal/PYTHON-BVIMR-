
month = input("Enter month name: ").strip().lower()

if month in ("december", "january", "february"):
    print("Season: Winter")
elif month in ("march", "april", "may"):
    print("Season: Summer")
elif month in ("june", "july", "august", "september"):
    print("Season: Monsoon")
elif month in ("october", "november"):
    print("Season: Autumn")
else:
    print("Invalid month name!")

from Signature_folder.Signature import sign
sign()