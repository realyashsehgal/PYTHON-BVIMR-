text = "  hello world  "

print("Original:", repr(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())
print("Stripped:", text.strip())
print("Replaced:", text.replace("world", "Yash"))
print("Split:", text.split())
print("Joined:", "-".join(["Python", "is", "fun"]))
print("Starts with 'he':", text.strip().startswith("he"))
print("Ends with 'ld':", text.strip().endswith("ld"))

from Signature_folder.Signature import sign
sign()