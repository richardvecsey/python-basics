"""
Comparsion two lists and get back common elements
"""

a_list = [0, 1, 2, 3, 4, 5]
b_list = [3, 4, 5, 6, 7, 8]

# Get the common items:
common_values_1 = set(a_list).intersection(b_list)
print('Common items: {}'.format(common_values_1))

# Get the count of common items
count_common_values_1 = len(set(a_list).intersection(b_list))
print('Count: {}'.format(count_common_values_1))

# Get the common items:
common_values_2 = set(a_list) & set(b_list)
print('\nCommon items with second method: {}'.format(common_values_2))

# Get the common items:
common_values_3 =  set(a_list) - (set(a_list) - set(b_list))
print('\nCommon items with third method: {}'.format(common_values_3))

# If you want to get back a list, use list() function:
common_values_4 = list(set(a_list).intersection(b_list))
print('\nThis is a list: {}'.format(common_values_4))
