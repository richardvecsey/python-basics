"""
Get the harmonic mean of numbers
--------------------------------
Input:      (list) numbers

Output:     (float) harmonic mean of numbers
"""
from statistics import harmonic_mean


numbers = [20, 10, 5]
mean_1 = harmonic_mean(numbers)
print('original numbers: {}\nmean: {}'.format(numbers, mean_1))

numbers_2 = [20.0, 10.0, 5.0]
mean_2 = harmonic_mean(numbers_2)
print('\noriginal numbers: {}\nmean: {}'.format(numbers_2, mean_2))

numbers_3 = [10, 10, 10]
mean_3 = harmonic_mean(numbers_3)
print('\noriginal numbers: {}\nmean: {}'.format(numbers_3, mean_3))
