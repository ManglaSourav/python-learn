# Objects: Everything in Python is an object.
# Even values of basic primitive types(integer, string, float..) are objects.
# Lists are objects, tuples, dictionaries, everything.
age = 5
# The id() global function provided by Python lets you inspect the location in
# memory for a particular object.
print(id(age))
print(id(age))
age = age + 1
print(id(age))


# loops

count = 0
while count < 10:
    print("The condition is True")
    count = count + 1

print("After the loop")

items = [1, 2, 3, 4]
for item in items:
    print(item)

for item in range(4):
    print(item)

items = [1, 2, 3, 4]
for index, item in enumerate(items):  # to get the index
    print(index, item)

# Both while and for loops can be interrupted inside the block, using two special keywords: break and continue.
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue
    elif item == 3:
        break
    print(item)


# classes

class Dog:
    # the Dog class
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    # self as the argument of the method points to the current object instance, and must be specified when defining a method.
    def bark(self):
        print('WOF!')


roger = Dog('Roger', 8)
print(type(roger))
print(roger.name)
roger.bark()


# One important features of classes is inheritance.
class Animal:
    def walk(self):
        print('Walking..')


class Cat(Animal):  # the Cat class can inherit from Animal:
    def Meow(self):
        print('Meow!')


cat = Cat()
cat.walk()


# Lambda Functions:
# Lambda functions (also called anonymous functions) are tiny functions that have no name and only have one expression as their body.
# The body must be a single expression. Expression, not a statement.
# This difference is important. An expression returns a value, a statement does not.

# Lambda functions can accept more arguments:
# lambda a, b: a * b

# multiply = lambda a, b : a * b
multiply = lambda a, b : a * b
print(multiply(2, 2))