"""
Get a reverse of list
---------------------

Input:      (list)  original list

Return:     None

Output:     list    update the original lsit with the reversed elements    
"""

# Original list
cars = ["Audi", "BMW", "Chrysler", "Dodge"]
print('Original list: {}'.format(cars))

# Using [::-1] slice operator to get back the reversed list 
reverse_1 = cars[::-1]
print('\nReversed list (1): {}'.format(reverse_1))

# Reverse function does not have any return value.
# It updates the list with the reversed elements.
# reverse_2 is used for demonstration purpose
# since function is inplace, the "cars.reverse()" is enough to use
reverse_2 = cars.reverse()
print('\nReversed list (2): {}'.format(cars))
print('The return value of function is: {}'.format(reverse_2))
