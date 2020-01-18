"""
Return the boolean value of an object
-------------------------------------
Input   (object)    any object

Return  (boolean)   Always True, except:
                    - obejct is None
                    - object is empty
                    - object is False
                    - object is 0
"""
# List contains elements
cars = ["Audi", "BMW", "Chrysler", "Dodge"]
boolean_cars = bool(cars)
print('Object: {}\nBoolean: {}'.format(cars, boolean_cars))

# Empty list
empty_list = []
boolean_empty_list = bool(empty_list)
print('\nObject: {}\nBoolean: {}'.format(empty_list, boolean_empty_list))

# Integer
number = 25
boolean_number = bool(number)
print('\nObject: {}\nBoolean: {}'.format(number, boolean_number))

# Zero
zero_number = 0
boolean_zero_number = bool(zero_number)
print('\nObject: {}\nBoolean: {}'.format(zero_number, boolean_zero_number))