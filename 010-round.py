"""
Round a number
--------------
Input   (float)     A floating point number
        (int)       Number of decimals
                    Default value is: 0
Output  (float)     Rounded number
        (int)       Whether using the default decimals value, the return number
                    will be the nearest integer
"""

number = 103.14159

# Rounding with 2 decimals
number_rounded = round(number, 2)
print('Rounding with 2 decimals')
print('original number: {}, rounded: {}, type of rounded: {}'
      .format(number, number_rounded, type(number_rounded)))

# Rounding with -2 decimals
number_rounded = round(number, -2)
print('\nRounding with -2 decimals')
print('original number: {}, rounded: {}, type of rounded: {}'
      .format(number, number_rounded, type(number_rounded)))

# Rounding with 0 decimals
number_rounded = round(number, 0)
print('\nRounding with 0 decimals')
print('original number: {}, rounded: {}, type of rounded: {}'
      .format(number, number_rounded, type(number_rounded)))

# Rounding with default
# Result will be integer (!)
number_rounded = round(number)
print('\nRounding with default')
print('original number: {}, rounded: {}, type of rounded: {}'
      .format(number, number_rounded, type(number_rounded)))
