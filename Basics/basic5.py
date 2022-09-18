# Introspection :Functions, variables and objects can be analyzed using introspection.

# function introspection
def increment(n):
    return n + 1


print(increment)
# help(increment)
print(type(increment))


# an object:
class Dog():
    def bark(self):
        print('WOF!')


roger = Dog()
print(roger)
# help(roger)
print(type(roger))
'''The dir() global function lets us find out all the methods 
and attributes of an object:'''
print(dir(roger))
'''The id() global function shows us the location in memory of any object:'''
print(id(roger))


print(type(1))


# Annotations
'''
Python is dynamically typed. We do not have to specify the type 
of a variable or function parameter, or a function return value.
'''


def increment(n):
    return n + 1

# This is the same function with annotations:
# def increment(n: int) -> int:
#     return n + 1


# You can also annotate variables:
count: int = 0


# Exceptions


try:
    # raise Exception('An error occurred!')
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')
else:
    print("no exception occured")
    # no exceptions were raised, the code ran successfully
finally:
    result = 1

print(result)


# with statement : with makes this process transparent.


filename = 'sample.txt'

try:
    file = open(filename, 'r')
    content = file.read()
    print(content)
finally:
    file.close()

# In other words we have built-in implicit exception handling,
# as close() will be called automatically for us.
with open(filename, 'r') as file:
    content = file.read()
    print(content)
