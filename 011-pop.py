"""
Remove item from a list
-----------------------
Input   (int)   index of removed element
                default: -1
                
Output          removed element
"""

# Remove the last element
print("Remove the last element:")
cars = ["Audi", "BMW", "Chrysler", "Dodge"]
print('Original list: {}'.format(cars))
cars.pop()
print('Original list: {}'.format(cars))

# Remove a specific element: first
print("\nRemove a specific element: first")
cars = ["Audi", "BMW", "Chrysler", "Dodge"]
print('Original list: {}'.format(cars))
cars.pop(0)
print('Original list: {}'.format(cars))

# Remove a specific element: second
print("\nRemove a specific element: second")
cars = ["Audi", "BMW", "Chrysler", "Dodge"]
print('Original list: {}'.format(cars))
cars.pop(1)
print('Original list: {}'.format(cars))

# Remove and get a specific element: second
print("\nRemove and get a specific element: second")
cars = ["Audi", "BMW", "Chrysler", "Dodge"]
print('Original list: {}'.format(cars))
removed = cars.pop(1)
print('Original list: {}'.format(cars))
print('Removed element: {}'.format(removed))