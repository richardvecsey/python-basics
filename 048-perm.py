"""
Number of possibilities to choose k items from n items without repetition with order
------------------------------------------------------------------------------------
Input:      n   (int)   number of all elements
            k   (int)   number of elements to choose
                        whether k = None, function returns n!

Output:     (int)       number of possibilities
                        n! / (n - k)! when k < n
                        n! when k = None
                        0 when k > n
"""
# This function is available from Python 3.8

from math import perm

# You have a deck contained 52 cards. You should select 5 of them.
# How many ways can 5 cards be chosen?

n = 52 # size of deck
k = 5  # number of selection

# NOTE: Permutation isn't equals to combination. If you want to calculate
# chance, use combination instead of permutation.
# Result of combination: 2,598,960 
result = perm(n, k)
print('You can pick {} cards from {} carded deck in {} different ways.'
      .format(k, n, result))