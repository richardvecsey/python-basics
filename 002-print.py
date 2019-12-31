"""
Print something onto the screen. The screen does mean console, terminal or
command line.
--------------------------------------------------------------------------
Output:        (text)        message
"""

from time import sleep

# The message should be between parentheses in Python 3.x
print('This is a message.')

# Adding two texts
a = "too."
print('This is a message ' + a)

# Formatting is allowed
b = 'third'
print('This is the {} message.'.format(b))

# Printing multiple messages in the same line
for i in range(11):
    print('\rCounting: {:02d}'.format(i), end='')
    sleep(0.3)