"""
Get the arithmetic mean of numbers
----------------------------------
Input:      (list) numbers

Output:     (number) arithmetic mean of numbers
"""
from statistics import mean

numbers = [10, 5, 0, -5, -10]
mean_1 = mean(numbers)
print('original numbers: {}\nmean: {}'.format(numbers, mean_1))


numbers_2 = [10.0, 5.0, 0, -5.0, -10]
mean_2 = mean(numbers_2)
print('original numbers: {}\nmean: {}'.format(numbers_2, mean_2))
