from enum import Enum
from collections import Counter
# Enum


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State.ACTIVE)
print(State(1))
print(State['ACTIVE'])
print(State.ACTIVE.value)
print(list(State))
print(len(State))

# user input
# print("Enter something")
# something = input()
# print("this is something ", something)

a = 3
result = 2 if a == 2 else 3
print(result)


# List: A list can hold values of different types:
items = ["Roger", 1, "Syd", True]
print(items)
print("Roger" in items)
items[0] = "Roger"
print(items[0])

items.index("Roger")  # 0
items.index("Syd")  # 2
print(items[-1])  # True
print(items[0:2])
print(items)
items.append("Test1")
items.extend(["Test2"])
items += ["Test3"]
print(items)

# Tip: with extend() or += don’t forget the square brackets.
# Don’t do items += "Test" or items.extend("Test") or
# Python will add 4 individual characters to the list, resulting in ['Roger', 1, 'Syd', True, 'T', 'e', 's', 't']
# items.extend("Test")  # careful without brakets

items.remove("Test1")
print(items)
items.insert(1, "Test")  # add "Test" at index 1
print(items)
# To add multiple items at a specific index, you need to use slices:
items[1:1] = ["Test1", "Test2"]

# sort() will only work if the list holds values that can be compared. Strings and integers for example can’t be compared,
# items.sort()
# The sort() methods orders uppercase letters first, then lowercased letters. To fix this, use:
items.sort(key=str.lower)
# Sorting modifies the original list content. To avoid that, you can copy the list content using
# itemscopy = items[:]
# or use sorted method
# print(sorted(items, key=str.lower))
print(items)


# TUPLE: They allow you to create immutable groups of objects.
# This means that once a tuple is created, it can’t be modified. You can’t add or remove items.
names = ("Zer", "Roger", "Syd")
print(names)
print("Roger" in names)  # True
print(sorted(names))
newTuple = names + ("Vanille", "Tina")
print(newTuple)

# Dictionaries
# A dictionary can contain multiple key/value pairs:
dog = {'name': 'Roger', 'age': 8}

print(list(dog.keys()))  # only keys
print(dog.keys())  # return dict_key type data
print(list(dog.values()))  # only values
print(list(dog.items()))  # both keys and values

print(dog['name'])
dog['name'] = 'Syd'
print(dog.get('name'))  # 'Roger'
print(dog.get('test', 'default'))
print(dog)
dog.pop('name')  # method retrieves and removes the key/value pair
print(dog)
# The popitem() method retrieves and removes the last key/value pair inserted into the dictionary:
dog.popitem()
print(dog)
dog['favorite food'] = 'Meat'  # add new pair
print(len(dog))
del dog['favorite food']  # delete a key/value pair
dogCopy = dog.copy()  # copy the dictionary

# Sets :  they work like tuples, but they are not ordered, and they are mutable
# They also have an immutable version, called frozenset.
set1 = {"Roger", "Syd"}
set2 = {"Roger"}
intersect = set1 & set2  # {'Roger'}
union = set1 | set2
difference = set1 - set2  # {'Syd'}
isSuperset = set1 > set2  # True
print(intersect, union, difference, isSuperset)
print(len(set1))
print("Roger" in set1)  # True
# list from the items in a set by passing the set to the list() constructor
print(list(set1))


# functions
def hello(name='my friend', age=0):  # default values
    print('Hello ' + name + '!')
    print("age", age)
    age = 1
    print("age", age)


age = 5
hello(age=age)
print(age)


# Counter is a subclass of dict that’s specially designed for counting hashable objects in Python.
# It’s a dictionary that stores objects as keys and counts as values. To count with Counter,
# you typically provide a sequence or iterable of hashable objects as an argument to the class’s constructor.
counter1 = Counter("mississippi")
counter2 = Counter(list("mississippiii"))
print(counter1 == counter2)
