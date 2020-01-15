"""
Get the number of items in an object
------------------------------------
Input:      object

Return:     number of items
"""

# Lenght of a list
cars = ["Audi", "BMW", "Chrysler", "Dodge"]
print('\nList: {}\nLenght of list: {}'.format(cars, len(cars)))

# Lenght of a dictionary
dictionary = {"name": "Alice", "age": "30"}
print('\nDictionary: {}\nLenght of dictionary: {}'.format(dictionary,len(dictionary)))

# Lenght of a string equals the number of characters
string = "This is a string."
print('\nString: {}\nLenght of string: {}'.format(string,len(string)))