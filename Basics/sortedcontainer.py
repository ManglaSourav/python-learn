# importing libraries
from sortedcontainers import SortedList, SortedSet, SortedDict

# initializing a sorted list with parameters
# it takes an iterable as a parameter.
sorted_list = SortedList([1, 2, 3, 4])

# initializing a sorted list using default constructor
sorted_list = SortedList()

# inserting values one by one using add()
for i in range(5, 0, -1):
    sorted_list.add(i)

# prints the elements in sorted order
print('list after adding 5 elements: ', sorted_list)

print('list elements are: ', end='')

# iterating through a sorted list
for i in sorted_list:
    print(i, end=' ')
print()

# removing all elements using clear()
sorted_list.clear()

# adding elements using the update() function
elements = [10, 9, 8, 7, 6]

sorted_list.update(elements)

# prints the updated list in sorted order
print('list after updating: ', sorted_list)

# removing a particular element
sorted_list.discard(8)

print('list after removing one element: ', sorted_list)

# removing all elements
sorted_list.clear()

print('list after removing all elements using clear: ', sorted_list)




# sorteddict
# initializing a sorted dict with parameters
# it takes a dictionary object as a parameter
sorted_dict = SortedDict({'a': 1, 'b': 2, 'c': 3})

# initializing a sorted dict
sorted_dict = SortedDict({'a': 1, 'c': 2, 'b': 3})

# print the dict
print('sorted dict is: ', sorted_dict)

# adding key => value pairs
sorted_dict['d'] = 3

print('sorted dict after adding an element: ', sorted_dict)

# adding element using setdefault()
sorted_dict.setdefault('e', 4)

print('sorted dict after setdefault(): ', sorted_dict)

# using the get function
print('using the get function to print the value of a: ', sorted_dict.get('a', 0))

# checking membership using 'in' operator
if('a' in sorted_dict):
    print('a is present')
else:
    print('a is not present')

print('dict elements are: ', end='')

# iterating over key => value pairs in a dictionary
for key in sorted_dict:
    print('{} -> {}'.format(key, sorted_dict[key]), end=' ')
print()

# removing all elements from the dict
sorted_dict.clear()

print('sorted dict after removing all elements: ', sorted_dict)
