"""
Get the absolute value of a number
----------------------------------
Input:      number

Output:     absolute value of number
"""

numbers = [1, 0.5, 0, -0.5, -1]
for i in numbers:
    abs_i = abs(i)
    print('original number: {} <-> absolute value: {}'.format(i, abs_i))

number = input('Give a number: ')
number = float(number)
print('original number: {} <-> absolute value: {}'.format(number, abs(number)))
print('')

# How can you code this process without using abs() function?
number = input('Give a number: ')
number = float(number)
# NOTE: There is no need o check number == 0 condition, since it is equal to
# the else
if number < 0:
    abs_number = number * -1
else:
    abs_number = number
print('original number: {} <-> absolute value: {}'.format(number, abs_number))    
