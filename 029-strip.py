"""
Remove any character(s) from the beginning and ending of a string
-----------------------------------------------------------------

Input:      (string)  base string
            (char)    Character(s) to remove
                      Default value: whitespace

Return:     (string)
"""
text = "abcd|<- The 'abcd' will be removed from the beginning and ending. ->|abcd"
print('\nOriginal text: "{}"'.format(text))
new_text = text.strip('abcd')
print('New text: "{}"'.format(new_text))

text_2 = "abcd|<- Only the first 'a' will be removed. ->|abcd"
print('\nOriginal text: "{}"'.format(text_2))
new_text_2 = text_2.strip('a')
print('New text: "{}"'.format(new_text_2))

text_3 = "abcd|<- Only the last 'd' will be removed. ->|abcd"
print('\nOriginal text: "{}"'.format(text_3))
new_text_3 = text_3.strip('d')
print('New text: "{}"'.format(new_text_3))

whitespace = "     |<- There is 5 white space at the beginning and ending. ->|     "
print('\nOriginal text: "{}"'.format(whitespace))
new_whitespace = whitespace.strip()
print('New text: "{}"'.format(new_whitespace))