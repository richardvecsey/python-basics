"""
Get the value of number to the power of another number
------------------------------------------------------

Input:      (number)  base               (x)
            (number)  exponent           (y)
            (int)     (optional) modulus (z)

Return:     number    the value of x to the power of y, modulus z
"""

number_x = 5
number_y = 3

print('Base: {}'.format(number_x))
print('Exponent: {}'.format(number_y))

# pow() without third parameter
res = pow(number_x, number_y)
print('pow() without third parameter: {}'.format(res))
print('type: {}'.format(type(res)))

number_x = 5
number_y = 3
number_z = 10

print('\nBase: {}'.format(number_x))
print('Exponent: {}'.format(number_y))
print('Modulus: {}'.format(number_z))

# pow() with third parameter
res = pow(number_x, number_y, number_z)
print('pow() without third parameter: {}'.format(res))
print('type: {}'.format(type(res)))

number_x = 5.0
number_y = 3.0
number_z = 4

print('\nBase: {}'.format(number_x))
print('Exponent: {}'.format(number_y))
print('Modulus: {} <- third parameter are allowed only when x and y are integers'.format(number_z))

# pow() without third parameter
# third parameter are allowed only when x and y are integers
res = pow(number_x, number_y)
print('pow() without third parameter: {}'.format(res))
print('type: {}'.format(type(res)))

number_x = 9
number_y = 0.5

print('\nBase: {}'.format(number_x))
print('Exponent: {}'.format(number_y))

# pow() without third parameter
# third parameter are allowed only when x and y are integers
res = pow(number_x, number_y)
print('pow() without third parameter: {}'.format(res))
print('type: {}'.format(type(res)))

number_x = 9.0
number_y = 0.5

print('\nBase: {}'.format(number_x))
print('Exponent: {}'.format(number_y))

# pow() without third parameter
# third parameter are allowed only when x and y are integers
res = pow(number_x, number_y)
print('pow() without third parameter: {}'.format(res))
print('type: {}'.format(type(res)))

number_x = -5.0
number_y = 0.5

print('\nBase: {}'.format(number_x))
print('Exponent: {}'.format(number_y))

# pow() without third parameter
# third parameter are allowed only when x and y are integers
res = pow(number_x, number_y)
print('pow() without third parameter: {}'.format(res))
print('type: {}'.format(type(res)))