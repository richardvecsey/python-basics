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
print('\noriginal numbers: {}\nmean: {}'.format(numbers_2, mean_2))

# How to calculate arithmetic mean without satistics.mean() function?
numbers_3 = [20.0, 10, 0, -5.0, -10]
sum_numbers = sum(numbers_3)
count_numbers = len(numbers_3)
mean_numbers = sum_numbers / count_numbers
print('\noriginal numbers: {}\nmean without function: {}'.format(numbers_3, mean_numbers))
