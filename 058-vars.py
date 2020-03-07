"""
Return the __dic__ attribute of an object
-----------------------------------------
Params:     object  (obj)   object with __dic__ attribute
            
Output:     dict    (dict)  dictionary containing the input object's
                            changable attributes
"""
class Person:
    
    name = 'Alice'
    age = '36'
    workplace = 'Office'


variables = vars(Person)

print(variables)