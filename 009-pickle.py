"""
Object serialization: save and load objects into a pickle file
"""
import pickle

cars = ["Audi", "BMW", "Chrysler", "Dodge"]  

# save list into a pickle file
pickle.dump(cars, open("cars.p", "wb"))

# load list from pickle into a variable
new_cars = pickle.load(open("cars.p", "rb"))

print(new_cars)