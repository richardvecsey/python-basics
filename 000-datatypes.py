"""
Demonstration of different data types in Python
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

print('Value: {},\nType: {},\nLenght: {}\n'.format(type01, type(type01), len(type01)))
print('Value: {},\nType: {}\n'.format(type02, type(type02)))
print('Value: {},\nType: {}\n'.format(type03, type(type03)))
print('Value: {},\nType: {},\nLenght: {}\n'.format(type04, type(type04), len(type04)))
print('Value: {},\nType: {},\nLenght: {}\n'.format(type05, type(type05), len(type05)))
print('Value: {},\nType: {},\nLenght: {}\n'.format(type06, type(type06), len(type06)))
print('Value: {},\nType: {},\nLenght: {}\n'.format(type07, type(type07), len(type07)))
print('Value: {},\nType: {},\nLenght: {}\n'.format(type08, type(type08), len(type08)))
print('Value: {},\nType: {}\n'.format(type09, type(type09)))
print('Value: {},\nType: {},\nLenght: {}\n'.format(type10, type(type10), len(type10)))
print('Value: {},\nType: {},\nLenght: {}\n'.format(type11, type(type11), len(type11)))
print('Value: {},\nType: {},\nLenght: {}\n'.format(type12, type(type12), len(type12)))
print('Value: {},\nType: {},\nLenght: {}\n'.format(type13, type(type13), len(type13)))