#. Write a python code to demonstrate multiple inputs, variable inputs and integer inputs and separate them by spaces.
# Taking multiple inputs separated by spaces
inputs = input("Enter multiple values separated by spaces: ").split()

# Variable number of inputs
print("You entered", len(inputs), "values:", inputs)

# Converting inputs to integers
int_inputs = list(map(int, inputs))
print("Integer values:", int_inputs)