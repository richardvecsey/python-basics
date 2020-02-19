"""
Swap cases in a string
----------------------
Input:      (string)    any string

Output:     (string)    swapped string, upper cases become lower cases and
                        vice versa
"""

original_string = 'This is an "A" letter.'
modified_string = original_string.swapcase()

print('original string: {}\nswapped version: {}'
      .format(original_string, modified_string))