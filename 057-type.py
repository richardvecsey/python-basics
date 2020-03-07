"""
Return type of a specified object
---------------------------------
Params:     object  (obj)   specified object that is the base of examination
            bases   (class) [optional] base class
            dict    (class) [optional] specifies the namespace
            
Output:     type    (type)  type of object
""" 

type01 = "Alice"
type02 = 10
type03 = 10.0
type04 = ["Alice", "Bob"]
type05 = ("Alice", "Bob")
type06 = {"name": "Alice", "age": "30"}
type07 = {"Alice", "Bob"}
type08 = frozenset({"Alice", "Bob"})
type09 = True
type10 = range(10)
type11 = b"Alice"
type12 = bytearray(10)
type13 = memoryview(bytes(10))

print('Value: {}\nType: {}\n'.format(type01, type(type01)))
print('Value: {}\nType: {}\n'.format(type02, type(type02)))
print('Value: {}\nType: {}\n'.format(type03, type(type03)))
print('Value: {}\nType: {}\n'.format(type04, type(type04)))
print('Value: {}\nType: {}\n'.format(type05, type(type05)))
print('Value: {}\nType: {}\n'.format(type06, type(type06)))
print('Value: {}\nType: {}\n'.format(type07, type(type07)))
print('Value: {}\nType: {}\n'.format(type08, type(type08)))
print('Value: {}\nType: {}\n'.format(type09, type(type09)))
print('Value: {}\nType: {}\n'.format(type10, type(type10)))
print('Value: {}\nType: {}\n'.format(type11, type(type11)))
print('Value: {}\nType: {}\n'.format(type12, type(type12)))
print('Value: {}\nType: {}\n'.format(type13, type(type13)))