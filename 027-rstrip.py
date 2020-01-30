"""
Remove any character(s) from the end of a string
------------------------------------------------

Input:      (string)  base string
            (char)    Character(s) to remove
                      Default value: whitespace

Return:     (string)
"""

text = "These are cars: Audi, BMW, Chrysler, Dodge."
print('Original text: {}\n'.format(text))
new_text = text.rstrip(', Dodge.')
print("New text: {}".format(new_text))
