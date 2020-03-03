"""
Calculate 2^n in O(1)
---------------------
This method based on shifting bits.
decimal | binary
      1     1
      2     10
      4     100
      8     1000
Adding an extra zero the end of binary number equals multiplying the decimal
value by 2.

operator used: '<<'
"""

base = 2
exponent = 3

result = base << (exponent - 1)
print('Base: {}\nExponent: {}\nResult: {}\n'.format(base, exponent, result))

# check with for cycle
result = base
for i in range((exponent - 1)):
    result *= base
print('Base: {}\nExponent: {}\nResult: {}\n'.format(base, exponent, result))    

# check with for pow()
result = pow(base, exponent)
print('Base: {}\nExponent: {}\nResult: {}\n'.format(base, exponent, result)) 