"""
A classic "Hello, World!" application in 8 different ways
---------------------------------------------------------

Update 01:  * add one more method, now 8 ways are available
            * correct typo



Output:    (text)    Print "Hello, World!" message in the console
"""

from time import sleep

# Print "Hello, World!"
print('Hello, World!')

# Print "Hello, World!" with using variable
a = 'Hello, World!'
print(a)

# Print "Hello, World!" with using an empty variable and adding the text later
a = ''
a += 'Hello, World!'
print(a)

# Print "Hello, World!" with formatting
a = 'Hello,'
b = ' World!'
print('{}{}'.format(a,b))

# Print "Hello, World!" with formatting and adding punctuation in the print()
a = 'Hello'
b = 'World'
print('{}, {}!'.format(a,b))

# Print "Hello, World!" with formatting and capitalizing
a = 'hello'
a = a.capitalize()
b = 'world'
c = b.capitalize()
print('{}, {}!'.format(a,c))

# Print "Hello, World!" with for loop iterate over list
letters = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
message = ''
for i in letters:
    message += i
print(message)

# Print "Hello, World!" with for loop iterate over string
original_message = 'Hello, World!'
message = ''
for i in original_message:
    message += i
    sleep(0.2)
    print('\r{}'.format(message), end='')
