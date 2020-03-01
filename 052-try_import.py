"""
Show example how to handle missing import
-----------------------------------------
This method is useful to handle missing import
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