from Signature_folder.Signature import sign

def get_even_numbers(n):
    evens = [i for i in range(1, n + 1) if i % 2 == 0]
    return evens

def student_info(name, age, course):
    info = {"Name": name, "Age": age, "Course": course}
    return info

print("Even Numbers:", get_even_numbers(10))

student = student_info("Yash", 21, "Data Science")
print("Student Info:", student)

sign()
