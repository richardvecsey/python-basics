"""
Iterate over a sequence. Sequence can be range, list, tuple, dictionary, set
or string
----------------------------------------------------------------------------
"""

print("Iterate over a range:")
for i in range(3): # i is a veriable, you can name it anything
    print(i)
    
print("\nIterate over a range; part 2:")
for i in range(3,11): # i is a veriable, you can name it anything
    print(i)

print("\nIterate over a range; part 3:")
for i in range(3,11,2): # i is a veriable, you can name it anything
    print(i)


print("\nIterate over a list:")
cars = ["Audi", "BMW", "Chrysler", "Dodge"]    
for car in cars:
    print(car)
    
print("\nThe break statement:")
for car in cars:
    print(car)
    if car == "BMW":
        print("'BMW' found, breaking the loop")
        break