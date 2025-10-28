#Write python code to create and access nested tuples.
# creating a nested tuple
student = ("Yash", (21, "Data Science"), ("India", "Delhi"))

# accessing elements
print("Name:", student[0])
print("Age:", student[1][0])
print("Course:", student[1][1])
print("Country:", student[2][0])
print("City:", student[2][1])
