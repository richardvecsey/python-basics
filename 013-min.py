"""
Get the lowest value from an iterable
-------------------------------------
Input:      iterable

Return:     lowest value
"""

numbers = [6, 5, 2, -1, 0, 1, 2, 3, 4, 5]
print('list: {}\n min: {}'.format(numbers, min(numbers)))

floats = [6.0, 5.1, 2.0, -1.0, 0.5, 1.9, 2.8, 3.4, 4.6, 5.1]
print('\nlist: {}\n min: {}'.format(floats, min(floats)))

cars = ["Ford", "Audi", "BMW", "Chrysler", "Dodge"]
print('\nlist: {}\n min: {}'.format(cars, min(cars)))