"""
Return True if all elements in iterable are true
------------------------------------------------
Input   (iterable)  iterable object

Return  (boolean)   True, when:
                    - all items are true
                    - object is empty
"""
# List contains elements
cars = ["Audi", "BMW", "Chrysler", "Dodge"]
all_cars = all(cars)
print('Object: {}\nAll: {}'.format(cars, all_cars))

# Empty list
empty_list = []
all_empty_list = bool(empty_list)
print('\nObject: {}\nAll: {}'.format(empty_list, all_empty_list))

# Tuple
test_tuple = (0, 0, 1)
all_test_tuple = all(test_tuple)
print('\nObject: {}\nAll: {}'.format(test_tuple, all_test_tuple))

# Tuple 2
test_tuple_2 = (25, 25, 25)
all_test_tuple_2 = all(test_tuple_2)
print('\nObject: {}\nAll: {}'.format(test_tuple_2, all_test_tuple_2))

# Dictionary
dictionary = {"name": "Alice", "age": "30"}
all_dictionary = all(dictionary)
print('\nObject: {}\nAll: {}'.format(dictionary, all_dictionary))

# Dictionary 2
dictionary_2 = {"name": True, "age": False}
all_dictionary_2 = all(dictionary_2)
print('\nObject: {}\nAll: {}'.format(dictionary_2, all_dictionary_2))

# Dictionary 3
dictionary_3 = {0: "Alice", 1: "name"}
all_dictionary_3 = all(dictionary_3)
print('\nObject: {}\nAll: {}'.format(dictionary_3, all_dictionary_3))