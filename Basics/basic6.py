# List comprehensions :List comprehensions are a way to create lists in a very concise way.

numbers = [1, 2, 3, 4, 5]
numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)

'''List comprehensions are a syntax that’s sometimes preferred over 
loops, as it’s more readable when the operation can be written on a 
single line:
'''

numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)

# and over map():
numbers_power_2 = list(map(lambda n: n**2, numbers))

# Polymorphism :Polymorphism generalizes a functionality so it can work on different types.

# We can define the same method on different classes:


class Dog:
    def eat(self):
        print('Eating dog food')


class Cat:
    def eat(self):
        print('Eating cat food')


animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()
# We built a generalized interface and we now do not need to know that an animal is a Cat or a Dog


# Operator Overloading
class Doggy:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return True if self.age > other.age else False


roger = Doggy('Roger', 8)
syd = Doggy('Syd', 7)
print(roger > syd)  # greater than operator working with objects

"""
In the same way we defined __gt__() (which means greater than), we can define the following methods:

__eq__() to check for equality
__lt__() to check if an object should be considered lower than another with the < operator
__le__() for lower or equal (<=)
__ge__() for greater or equal (>=)
__ne__() for not equal (!=)
Then you have methods to interoperate with arithmetic operations:

__add__() respond to the + operator
__sub__() respond to the – operator
__mul__() respond to the * operator
__truediv__() respond to the / operator
__floordiv__() respond to the // operator
__mod__() respond to the % operator
__pow__() respond to the ** operator
__rshift__() respond to the >> operator
__lshift__() respond to the << operator
__and__() respond to the & operator
__or__() respond to the | operator
__xor__() respond to the ^ operator
        """


""" 
Virtual Environments
It is common to have multiple Python applications running on your system.

When applications require the same module, at some point you will reach a tricky situation where an app needs a version of a module, and another app a different version of that same module.

To solve this, you use virtual environments.

We wll use venv. Other tools work similarly, like pipenv.

Create a virtual environment using

python -m venv .venv
in the folder where you want to start the project, or where you already have an existing project.

Then run

source .venv/bin/activate
Use source .venv/bin/activate.fish on the Fish shell

Executing the program will activate the Python virtual environment. Depending on your configuration you might also see your terminal prompt change.


     """
