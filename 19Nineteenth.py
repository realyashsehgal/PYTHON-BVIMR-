#Q19. Write python code to print all the leap years from year 1-2025. Also print the total count. 
from Signature_folder.Signature import sign
leap_years = []
for year in range(1, 2026):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_years.append(year)

print("Leap years from 1 to 2025:")
for year in leap_years:
    print(year)
print("Total count:", len(leap_years))
sign()