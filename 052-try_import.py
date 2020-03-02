"""
Show example how to handle missing import
-----------------------------------------
This method is useful to handle missing import

update 1: Add real life example with mean and fmean from statistics
          It helps to create a code that runs faster with python 3.8, but also
          works with python 3.x
"""

failed = []
success = []

try:
    import cv2
    success.append('cv2')
except:
    failed.append('cv2')
    
try:
    import sys
    success.append('sys')
except:
    failed.append('sys')

try:
    import numpy
    success.append('numpy')
except:
    failed.append('numpy')
    
for i in success:
    print('{} loaded successfully'.format(i))

for i in failed:
    print('{} failed'.format(i))
    

# Real life example
# fmean() is fester but available only from python 3.8
fmean_loaded = False

# Try to load statistics.fmean
try:
    from statistics import fmean
    fmean_loaded = True
# If it fails, loaded statistics.mean
except:
    from statistics import mean

# Two ways to calculate mean based on result of import
numbers = [20, 5, 0, -5, -10]
if fmean_loaded:
    mean = fmean(numbers)
else:
    mean = mean(numbers)

print('\nOriginal numbers: {}\nmean: {}'.format(numbers, mean))
if fmean_loaded:
    print('calculated by fmean()')
else:
    print('calculated by mean()')