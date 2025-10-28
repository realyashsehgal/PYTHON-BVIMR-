#Write python code to access and remove dictionary element.
# creating a dictionary
person = {"name": "Yash", "age": 21, "city": "Delhi"}

# accessing a value
print("Name:", person["name"])

# removing a key-value pair
removed_value = person.pop("city")

print("Removed:", removed_value)
print("Updated Dictionary:", person)
