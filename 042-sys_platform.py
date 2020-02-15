"""
Check operation system
----------------------
Input:      (None)

Output:     (string)    String contains name of platform.
"""
from sys import platform

# Use this function to create program depending on type of operation system
print('OS name: {}'.format(platform))
