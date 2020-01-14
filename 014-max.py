"""
Get the highest value from an iterable
--------------------------------------
Input:      iterable

Return:     highest value
"""

numbers = [6, 5, 2, -1, 0, 1, 2, 3, 4, 5]
print('list: {}\n max: {}'.format(numbers, max(numbers)))

floats = [6.0, 5.1, 2.0, -1.0, 0.5, 1.9, 2.8, 3.4, 4.6, 5.1]
print('\nlist: {}\n max: {}'.format(floats, max(floats)))

cars = ["Ford", "Audi", "BMW", "Chrysler", "Dodge"]
print('\nlist: {}\n max: {}'.format(cars, max(cars)))