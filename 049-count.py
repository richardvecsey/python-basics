"""
Counting elements in a collection with a specific value
-------------------------------------------------------
Input:      (object)    Any type of input object: list, tuple, string
            (value)     The value to search for.
                        Any type: list, tuple, string, number,

Return:     (int)       number of items
"""

# Numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 9, 8, 0]
search_value = 9
returnvalue = numbers.count(search_value)
print('\nNumbers: {}\nSearch value: {}\nCount: {}'
      .format(numbers, search_value, returnvalue))

# Cars in a list
cars = ["Audi", "BMW", "Chrysler", "Dodge", "Ford", "Ford"]
search_value = 'Ford'
returnvalue = cars.count(search_value)
print('\nCars: {}\nSearch value: {}\nCount: {}'
      .format(cars, search_value, returnvalue))

# Sentence
sentence = 'This is an "I" letter.'
search_value = 'i'
returnvalue = sentence.count(search_value)
print('\nSentence: {}\nSearch value: {}\nCount: {}'
      .format(sentence, search_value, returnvalue))

# Sentence
sentence = 'This is an "I" letter.'
sentence = sentence.lower()
search_value = 'i'
returnvalue = sentence.count(search_value)
print('\nSentence: {}\nSearch value: {}\nCount: {}'
      .format(sentence, search_value, returnvalue))

# Sentence
sentence = 'This is an "I" letter.'
search_value = 'is'
returnvalue = sentence.count(search_value)
print('\nSentence: {}\nSearch value: {}\nCount: {}'
      .format(sentence, search_value, returnvalue))

# Sentence
sentence = 'This is an "I" letter.'
search_value = 'an'
returnvalue = sentence.count(search_value)
print('\nSentence: {}\nSearch value: {}\nCount: {}'
      .format(sentence, search_value, returnvalue))