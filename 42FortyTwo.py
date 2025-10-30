
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {lst}")

print(f"lst[2:5] = {lst[2:5]}")       # Elements 2,3,4
print(f"lst[:3] = {lst[:3]}")         # First 3 elements
print(f"lst[5:] = {lst[5:]}")         # From index 5 to end
print(f"lst[:] = {lst[:]}")           # Complete copy

print(f"lst[-3:] = {lst[-3:]}")       # Last 3 elements
print(f"lst[:-2] = {lst[:-2]}")       # All except last 2

print(f"lst[::2] = {lst[::2]}")       # Every 2nd element
print(f"lst[1::3] = {lst[1::3]}")     # Every 3rd starting from index 1

print(f"lst[::-1] = {lst[::-1]}")     # Reverse entire list
print(f"lst[7:2:-1] = {lst[7:2:-1]}")  # Reverse from 7 to 3
from Signature_folder.Signature import sign
sign()
