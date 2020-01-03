"""
Looping as long as a condition is True
"""

print("Classic while loop example:")
i = 0
while i < 5:
  print(i)
  i += 1


print("\nLooping till BMW is founded")
cars = ["Audi", "BMW", "Chrysler", "Dodge"]
carindex = 0
car_not_found = True
while car_not_found:
    print(cars[carindex])
    if cars[carindex] == "BMW":
        print("'BMW' found, breaking the loop")
        car_not_found = False
    carindex += 1        