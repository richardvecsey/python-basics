"""
Get quotient and remainder of two non-complex numbers
-----------------------------------------------------
Input:      x   (number)    any non-complex number
            y   (number)    any non-complex number
Output:     w,z (tuple)     tuple[0] quotient
                            tuple[1] remainder

NOTE: Results inherit the type of inputs. If one of inputs is float, results
      are float too.
"""
x = 8
y = 3
result = divmod(x, y)
print('x = {}\ny = {}\ndivmod = {}\nquotient = {}\nremainder = {}\n'
      .format(x, y, result, result[0], result[1]))

x = 10.0
y = 2
result = divmod(x, y)
print('x = {}\ny = {}\ndivmod = {}\nquotient = {}\nremainder = {}\n'
      .format(x, y, result, result[0], result[1]))

x = 9.9
y = 2.1
result = divmod(x, y)
print('x = {}\ny = {}\ndivmod = {}\nquotient = {}\nremainder = {}\n'
      .format(x, y, result, result[0], result[1]))