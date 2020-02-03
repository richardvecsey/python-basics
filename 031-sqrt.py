"""
Get the square root of a number
-------------------------------
Input:      (number) non-negative number

Output:     (float)  square root of a number
"""

from math import sqrt

numbers = [99, 9, 4, 4.0, 0]
for i in numbers:
    sqrt_i = sqrt(i)
    print('original number: {} <-> square root value: {}'.format(i, sqrt_i))

number = input('Give a number: ')
number = float(number)
print('original number: {} <-> square root value: {}'.format(number, sqrt(number)))
print('')

