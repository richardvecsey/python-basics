"""
Test part of a code
-------------------
Input:      (code)      Part of a code for testing

Output:     (None)      None

Return:     (anything)  Handle error in except block
"""

# Function below throws error since variable named 'something' isn't defined
# print(something)

# Example 1
# When running code in try block fails, except block runs
print('Example 1')
try:
    print(something)
except:
    print('An error occured: variable named \'something\' isn\'t defined')


# Example 2
try:
    print('\nExample 2')
except:
    print('An error occured: variable named \'something\' isn\'t defined')
else:
    print('Using else block cause try block does not generate error')
    
# Example 3
# Finally block always runs
print('\nExample 3, part 1')    
try:
    print(something)
except:
    print('An error occured: variable named \'something\' isn\'t defined')    
finally:
    print('Finally block runs when try block raises error')

try:
    print('\nExample 3, part 2')
except:
    print('An error occured: variable named \'something\' isn\'t defined')
finally:
    print('Finally block runs when try block doesn\'t raise error')