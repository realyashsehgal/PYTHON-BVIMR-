from datetime import datetime
from Signature_folder.Signature import sign
def calculate_age(birth_date_str, given_date_str):
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    given_date = datetime.strptime(given_date_str, "%Y-%m-%d")
    age = given_date.year - birth_date.year
    if (given_date.month, given_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birth_date = input("Enter your birth date (YYYY-MM-DD): ")
given_date = input("Enter the given date (YYYY-MM-DD): ")
print("Your age on", given_date, "is:", calculate_age(birth_date, given_date))
sign()