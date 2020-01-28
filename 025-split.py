"""
Split a string into a list by a specific separator
--------------------------------------------------

Input:      (char)  separator
                    Default: whitespace
            (int)   [optional] maxsplit: how many split to get back
                    Default value = -1 (means all)

Return:     (list)  splitted list
"""

text = "These are cars: Audi, BMW, Chrysler, Dodge."

print('Original text: {}\n'.format(text))

# Separate by comma
splitted_text = text.split(",")
print('Separate by comma:')
print(splitted_text)

# Separate by whitespace
splitted_text_2 = text.split(" ")
print('\nSeparate by whitespace:')
print(splitted_text_2)

# Separate by default whitespace
splitted_text_3 = text.split()
print('\nSeparate by default whitespace:')
print(splitted_text_3)

# Separate by whitespace
# using "2" as maxsplit get back 3 elements
splitted_text_4 = text.split(" ", 2)
print('\nSeparate by whitespace using "2" as maxsplit:')
print(splitted_text_4)

# Separate by letter "a"
text_5 = "Anaconda"
splitted_text_5 = text_5.split("a")
print('\nOriginal text: {} splitted by letter "a"'.format(text_5))
print(splitted_text_5)

# Separate by letter "a"
text_6 = "Anacondas"
splitted_text_6 = text_6.split("a")
print('\nOriginal text: {} splitted by letter "a"'.format(text_6))
print(splitted_text_6)