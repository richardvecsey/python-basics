"""
Inherit all methods and properties from another class
-----------------------------------------------------
A class (child class or derived class) inherits properties, methods and
functions from another class (parent class or base class).
"""
# Parent class
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def printpersondata(self):
        print('Firstname: {}\nLastname: {}\nAge: {}\n'
              .format(self.firstname, self.lastname, self.age))

# Child class
# This class inherits printpersondata() from Person class
class Worker(Person):
    def __init__(self, firstname, lastname, age):
        super().__init__(firstname, lastname, age)

# Create a Worker
person_1 = Worker('Alice', 'Smith', '36')
person_1.printpersondata()