"""
Convert collections into an enumerate object
--------------------------------------------
Input: collection

Output: enumerate object (counter + collection)
"""

print('for loop with range() and len() functions')
cars = ["Audi", "BMW", "Chrysler", "Dodge"]  
for i in range(len(cars)):
    print('{} - {}'.format(i, cars[i]))

print('\nfor loop iterate over list and using external counter variable')    
count = 0    
for car in cars:
    print('{} - {}'.format(count, car))
    count += 1
    
print('\nfor loop with enumerate() function gives back the count and the element')    
for count, car in enumerate(cars):
    print('{} - {}'.format(count, car))
    
print('\nfor loop with enumerate() start value set to different than zero')    
for count, car in enumerate(cars, 1):
    print('{} - {}'.format(count, car))    