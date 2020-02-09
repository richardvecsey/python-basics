"""
Get the geometric mean of numbers
----------------------------------
Input:      (iterable) numbers

Output:     (float) geometric mean of numbers
"""
# Python 3.8 is required

from statistics import geometric_mean


numbers = [20, 5, 1]
mean_1 = geometric_mean(numbers)
print('original numbers: {}\nmean: {}'.format(numbers, mean_1))

numbers_2 = [20.0, 5.0, 1]
mean_2 = geometric_mean(numbers_2)
print('\noriginal numbers: {}\nmean: {}'.format(numbers_2, mean_2))

numbers_3 = [10, 10, 10]
mean_3 = geometric_mean(numbers_3)
print('\noriginal numbers: {}\nmean: {}'.format(numbers_3, mean_3))
