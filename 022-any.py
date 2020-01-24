"""
Return True if any elements in iterable are true
------------------------------------------------
Input   (iterable)  iterable object

Return  (boolean)   True, when:
                    - any items are true
                    False:
                    - otherwise
                    - object is empty
"""
# List contains elements
cars = ["Audi", "BMW", "Chrysler", "Dodge"]
any_cars = any(cars)
print('Object: {}\nAny: {}'.format(cars, any_cars))

# Empty list
empty_list = []
any_empty_list = any(empty_list)
print('\nObject: {}\nAny: {}'.format(empty_list, any_empty_list))

# Tuple
test_tuple = (0, 0, 1)
any_test_tuple = any(test_tuple)
print('\nObject: {}\nAny: {}'.format(test_tuple, any_test_tuple))

# Tuple 2
test_tuple_2 = (0, 0, 0)
any_test_tuple_2 = any(test_tuple_2)
print('\nObject: {}\nAny: {}'.format(test_tuple_2, any_test_tuple_2))

# Dictionary
dictionary = {"name": "Alice", "age": "30"}
any_dictionary = any(dictionary)
print('\nObject: {}\nAny: {}'.format(dictionary, any_dictionary))

# Dictionary 2
dictionary_2 = {"name": True, "age": False}
any_dictionary_2 = any(dictionary_2)
print('\nObject: {}\nAny: {}'.format(dictionary_2, any_dictionary_2))

# Dictionary 3
dictionary_3 = {0: "Alice", 1: "name"}
any_dictionary_3 = any(dictionary_3)
print('\nObject: {}\nAny: {}'.format(dictionary_3, any_dictionary_3))