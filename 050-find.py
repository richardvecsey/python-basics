"""
Search for a specific character in a string
-------------------------------------------
Input:      (string)    Any type of input object: list, tuple, string

Params:     value   (string)    String to search for
            start   (int)       [optional] Where to start the search
                                default: 0
            end     (int)       [optional] Where to end the search
                                default: end of the string

Return:     (int)       place of the first occurance
            -1          value not found
            
NOTE: find() and index() method are similar. If there s an occurance, they both
      returns with the same value. However, if value not found, find() returns
      with -1, index() raises an exception
"""

# Sentence
sentence = 'This is an "I" letter.'
search_value = 'i'
returnvalue = sentence.find(search_value)
print('\nSentence: {}\nSearch value: {}\nReturn: {}'
      .format(sentence, search_value, returnvalue))

# Sentence
sentence = 'This is an "I" letter.'
search_value = 'i'
returnvalue = sentence.find(search_value, 3)
print('\nSentence: {}\nSearch value: {}\nReturn: {}'
      .format(sentence, search_value, returnvalue))

# Sentence
sentence = 'This is an "I" letter.'
search_value = 'q'
returnvalue = sentence.find(search_value)
print('\nSentence: {}\nSearch value: {}\nReturn: {}'
      .format(sentence, search_value, returnvalue))

# Sentence
sentence = 'This is an "I" letter.'
search_value = 'an'
returnvalue = sentence.find(search_value)
print('\nSentence: {}\nSearch value: {}\nReturn: {}'
      .format(sentence, search_value, returnvalue))