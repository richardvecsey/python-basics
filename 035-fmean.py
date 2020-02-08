"""
Get the arithmetic mean of numbers
----------------------------------
Input:      (list) numbers

Output:     (float) arithmetic mean of numbers
"""
# fmean() is faster, than mean() and always returns with float
# Python 3.8 is required

from statistics import fmean


numbers = [20, 5, 0, -5, -10]
mean_1 = fmean(numbers)
print('original numbers: {}\nmean: {}'.format(numbers, mean_1))

numbers_2 = [20.0, 5.0, 0, -5.0, -10]
mean_2 = fmean(numbers_2)
print('\noriginal numbers: {}\nmean: {}'.format(numbers_2, mean_2))

numbers_3 = [10, 10, 10]
mean_3 = fmean(numbers_3)
print('\noriginal numbers: {}\nmean: {}'.format(numbers_3, mean_3))
