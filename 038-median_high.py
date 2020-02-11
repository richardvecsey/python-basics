"""
Calculate median of numbers
---------------------------
Input:      (list) numbers

Output:     (number) median of numbers
                     whether the data is odd, return value is the middle number
                     whether the data is even, return value is the higher of the
                     two middle numbers
"""
from statistics import median_high


numbers = [20, 10, 5]
median_1 = median_high(numbers)
print('original numbers: {}\nmedian: {}'.format(numbers, median_1))

numbers_2 = [20.0, 10.0, 5.0]
median_2 = median_high(numbers_2)
print('\noriginal numbers: {}\nmedian: {}'.format(numbers_2, median_2))

numbers_3 = [1, 2, 3, 5]
median_3 = median_high(numbers_3)
print('\noriginal numbers: {}\nmedian: {}'.format(numbers_3, median_3))
