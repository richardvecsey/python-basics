"""
Calculate median of numbers
---------------------------
Input:      (list) numbers

Output:     (numer) median of numbers
"""
from statistics import median


numbers = [20, 10, 5]
median_1 = median(numbers)
print('original numbers: {}\nmedian: {}'.format(numbers, median_1))

numbers_2 = [20.0, 10.0, 5.0]
median_2 = median(numbers_2)
print('\noriginal numbers: {}\nmedian: {}'.format(numbers_2, median_2))

numbers_3 = [1, 2, 3, 5]
median_3 = median(numbers_3)
print('\noriginal numbers: {}\nmedian: {}'.format(numbers_3, median_3))
