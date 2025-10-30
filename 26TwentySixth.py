inputs = input("Enter multiple Numbers separated by Space: ").split()

print("You entered", len(inputs), "values:", inputs)

int_inputs = list(map(int, inputs))
print("Integer values:", int_inputs)

from Signature_folder.Signature import sign
sign()