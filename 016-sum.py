"""
Return sum of iterable and start value
--------------------------------------
Input:      value   optional: start value

Return:     sum of values
"""

numbers = [0, 1, 2, 3, 4, 5]
print('numbers: {}\n sum: {}'.format(numbers, sum(numbers)))

start_value = 10
print('numbers: {} + start value: {}\n sum: {}'.format(numbers, start_value, sum(numbers, start_value)))

numbers = [0, 1, 2, 3, 4, 5, -10]
print('numbers: {}\n sum: {}'.format(numbers, sum(numbers)))