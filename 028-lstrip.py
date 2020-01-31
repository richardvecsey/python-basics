"""
Remove any character(s) from the beginning of a string
------------------------------------------------------

Input:      (string)  base string
            (char)    Character(s) to remove
                      Default value: whitespace

Return:     (string)
"""

text = "These are cars: Audi, BMW, Chrysler, Dodge."
print('Original text: "{}"'.format(text))
new_text = text.lstrip('These are cars: ')
print('New text: "{}"'.format(new_text))


whitespace = "     |<- There is 5 white space before and zero after."
print('\nOriginal text: "{}"'.format(whitespace))
new_whitespace = whitespace.lstrip()
print('New text: "{}"'.format(new_whitespace))