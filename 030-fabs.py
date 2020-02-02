"""
Get the absolute value of a number
----------------------------------
Input:      number

Output:     (float) absolute value of number

Note:       What is the difference between abs() and math.fabs()?
            Fabs always return with float, abs return float or integer based on
            inputs.

"""

from math import fabs

numbers = [1, 0.5, 0, -0.5, -1]
for i in numbers:
    fabs_i = fabs(i)
    print('original number: {} <-> absolute value: {}'.format(i, fabs_i))

# This is an example the difference between abs and math.fabs
number = input('Give a number: ')
number_fabs = float(number)
number_abs = float(number)
# When the given number is integer, abs returns integer
if number_fabs % int(number_fabs) == 0:
    number_abs = int(number)
print('absolute value (abs): {}\nabsolute value (fabs): {}'.format(abs(number_abs), fabs(number_fabs)))
print('')
