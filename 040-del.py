"""
Delete variable or user-defined object
--------------------------------------
Input:      (None)

Output:     (None)

Return:     (None)  Delete object or variable
"""

# Create a dummy list named cars, filled with brands from car industry
cars = ["Audi", "BMW", "Chrysler", "Dodge"]

print('Cars: {}'.format(cars))

# Delete list named cars
del cars

try:
    print('Cars: {}'.format(cars))
except:
    print('Variable named cars is deleted.\n')



# Create a dummy class named CarsClass, contains a list named cars, filled
# with brands from car industry
class CarsClass():

    cars = ["Audi", "BMW", "Chrysler", "Dodge"]

    def function(self):
        print('Cars: {}'.format(cars))    
    
print(CarsClass)

# Delete class named CarsClass
del CarsClass

try:
    print('Cars: {}'.format(CarsClass))
except:
    print('Class named CarsClass is deleted.')