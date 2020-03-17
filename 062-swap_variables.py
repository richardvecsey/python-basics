"""
Swap variables
--------------
Example of swapping variables.
"""
# Declare variables in one step
# The method works if you create variables independently too, but this is fancy
variable_1, variable_2 = 1, 2
print('Original values:')
print('variable_1 = {}\nvariable_2 = {}'.format(variable_1, variable_2))

# Swapping
# It must be in the same line, otherwise the swapping won't work
variable_1, variable_2 = variable_2, variable_1
print('Variables after swapping:')
print('variable_1 = {}\nvariable_2 = {}\n'.format(variable_1, variable_2))

# Example of creating variables in two different lines
variable_3 = 3
variable_4 = 4
print('Original values:')
print('variable_3 = {}\nvariable_4 = {}'.format(variable_3, variable_4))

# Swapping
variable_3, variable_4 = variable_4, variable_3
print('Variables after swapping:')
print('variable_3 = {}\nvariable_4 = {}\n'.format(variable_3, variable_4))

# Example 3
variable_5, variable_6 = 5, 6
print('Original values:')
print('variable_5 = {}\nvariable_6 = {}'.format(variable_5, variable_6))

# This isn't swapping
variable_5 = variable_6
variable_6 = variable_5
print('Variables after bad example:')
print('variable_5 = {}\nvariable_6 = {}\n'.format(variable_5, variable_6))