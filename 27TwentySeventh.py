inputs = input("Enter multiple values separated by commas: ").split(',')

variable_inputs = [x.strip() for x in inputs]

integer_inputs = [int(x) for x in variable_inputs]

print("You entered:", ', '.join(variable_inputs))
print("As integers:", ', '.join(map(str, integer_inputs)))
from Signature_folder.Signature import sign
sign()