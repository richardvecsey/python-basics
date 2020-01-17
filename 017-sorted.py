"""
Get a sorted list of any iterable object
----------------------------------------

Input:      (iterable)  original iterable
            (boolean)   reverse     True -> descending order
                                    False -> ascending order
                        default: False
            (boolean)   key: Any function to decide the sorting order.

Return:     (list)    sorted iterable
"""

# Sort words
cars = ["Ford", "Audi", "BMW", "Chrysler", "Dodge"]
print('Original list: {}\nSorted list:{}'.format(cars, sorted(cars)))

# Sort numbers
numbers = [6, 5, 2, -1, 0, 1, 2, 3, 4, 5]
print('\nNumbers: {}\nSorted numbers: {}'.format(numbers, sorted(numbers)))

# Sort floats
floats = [6.0, 5.1, 2.0, -1.0, 0.5, 1.9, 2.8, 3.4, 4.6, 5.1]
print('\nFloats: {}\nSorted floats: {}'.format(floats, sorted(floats)))

# Sort words descending
cars = ["Ford", "Audi", "BMW", "Chrysler", "Dodge"]
print('Original list: {}\nSorted list (descending):{}'.format(cars, sorted(cars, reverse=True)))

# Sort numbers descending
numbers = [6, 5, 2, -1, 0, 1, 2, 3, 4, 5]
print('\nNumbers: {}\nSorted numbers (descending): {}'.format(numbers, sorted(numbers, reverse=True)))

# Sort floats descending
floats = [6.0, 5.1, 2.0, -1.0, 0.5, 1.9, 2.8, 3.4, 4.6, 5.1]
print('\nFloats: {}\nSorted floats (descending): {}'.format(floats, sorted(floats, reverse=True)))

# sorted() function using on list is similat like list.sort()
# However, list.sort() method can be used only on list, sorted() function
# accepts any iterable.