"""
Sum of the first n powers of 2 fast
----------------------------------
This method based on shifting bits.
operator used: '<<'
"""

how_many_numbers_to_add = 5

result = (1 << how_many_numbers_to_add) - 1
print('Base: {}\nHow many numbers to add: {}\nResult: {}\n'
      .format(2, how_many_numbers_to_add, result))

# check with for cycle
print('\ncheck with for cycle\n')
check_result = 0
for i in range(how_many_numbers_to_add):
    check_result += pow(2,i)
print('Base: {}\nHow many numbers to add: {}\nResult: {}\n'
      .format(2, how_many_numbers_to_add, check_result))