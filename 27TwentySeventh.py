#Q28. Write a python code to demonstrate multiple inputs, variable inputs and integer inputs and separate them by commas.
# Taking multiple inputs separated by commas
inputs = input("Enter multiple values separated by commas: ").split(',')

# Variable number of inputs
variable_inputs = [x.strip() for x in inputs]

# Converting inputs to integers
integer_inputs = [int(x) for x in variable_inputs]

print("You entered:", ', '.join(variable_inputs))
print("As integers:", ', '.join(map(str, integer_inputs)))