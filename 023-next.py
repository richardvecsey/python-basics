"""
Return the next item in an iterator
-----------------------------------
Input   (iterator)  iter() object
        (value)     [optional] default return value when iter reaches its end

Return  (value)     next item in the iterator
                    default value when iter reaches its end
                    without default value next() raises error when iter reaches
                    its end
"""
# Iterator contains a list
cars = iter(["Audi", "BMW", "Chrysler", "Dodge"])
cars_list = ["Audi", "BMW", "Chrysler", "Dodge"]
print('Cars: {}'.format(cars_list))
print('Iterator: {}'.format(cars))

next_cars = next(cars)
print('\nFirst "next_cars": {}'.format(next_cars))

next_cars = next(cars)
print('\nSecond "next_cars": {}'.format(next_cars))

next_cars = next(cars)
print('\nThird "next_cars": {}'.format(next_cars))

next_cars = next(cars)
print('\nFourth "next_cars": {}'.format(next_cars))

# Fifth iteration doesn't work because of the iterator contains only 4 items
# next_cars = next(cars)
# print('\nFifth "next_cars": {}'.format(next_cars))

# Using default values prevent iteration error
cars_2 = iter(["Audi", "BMW", "Chrysler", "Dodge"])
next_cars_2 = next(cars_2, "Ford") # 1
print('\n\nFirst "next_cars_2": {}'.format(next_cars_2))
next_cars_2 = next(cars_2, "Ford") # 2
print('\nSecond "next_cars_2": {}'.format(next_cars_2))
next_cars_2 = next(cars_2, "Ford") # 3
print('\nThird "next_cars_2": {}'.format(next_cars_2))
next_cars_2 = next(cars_2, "Ford") # 4
print('\nFourth "next_cars_2": {}'.format(next_cars_2))
next_cars_2 = next(cars_2, "Ford") # 5
print('\nFifth "next_cars_2": {}'.format(next_cars_2))
next_cars_2 = next(cars_2, "Ford") # 6
print('\nSixth "next_cars_2": {}'.format(next_cars_2))
next_cars_2 = next(cars_2, True) # 7
print('\nSeventh "next_cars_2": {}'.format(next_cars_2))