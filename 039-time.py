"""
Return current timestamp in seconds
-----------------------------------
Input:      (None)

Output:     (float) current timestamp in seconds
"""
from time import time

# epoch time start at: January 1, 1970, 00:00:00 (UTC)
actual_time = time()
print('actual timestamp: {}'.format(actual_time))

# You can use time() to calculate running time of functions.