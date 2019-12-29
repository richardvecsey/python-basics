"""
A classic "Hello, World!" application in 7 different ways
---------------------------------------------------------    

Output:    (text)    Print "Hello, World!" message in the console
"""

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

# Print "Hello, World!" with formatting and capitalazing
a = 'hello'
a = a.capitalize()
b = 'world'
c = b.capitalize()
print('{}, {}!'.format(a,c))

# Print "Hello, World!" with for loop
letters = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
message = ''
for i in letters:
    message += i
print(message)