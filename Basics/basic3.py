from lib import dog
import argparse
import sys


# or
# from lib.dog import bark


# modules: Every Python file is a module.

# from dog import bark #The first strategy lets us pick the things we need.
# import dog :The second strategy allows us to load everything defined in a file.
# The file dog.py contains this code:
# def bark():
#     print('WOF!')
# We can import this function from another file using import, and once we do, we can reference the function using the dot notation, dog.bark():
# dog.bark()
# Or, we can use the from .. import syntax and call the function directly:
dog.bark()

# breakpoint() # to dubug


'''
code formatting:
-Indent using spaces, not tabs
-Indent using 4 spaces.
-Python files are encoded in UTF-8
-Use maximum 80 columns for your code
-Write each statement on its own line
-Functions, variable names and file names are lowercase, with underscores between words (snake_case)
-Class names are capitalized, separate words are written with the capital letter too, (CamelCase)
-Package names are lowercase and do not have underscores between words
-Variables that should not change (constants) are written in uppercase
-Variable names should be meaningful
-Add useful comments, but avoid obvious comments
-Add spaces around operators
-Do not use unnecessary whitespace
-Add a blank line before a function
-Add a blank line between methods in a class
-Inside functions/methods, blank lines can be used to separate related blocks of code to help readability
'''


# command line arguments
print(len(sys.argv))
print(sys.argv)

# OR

parser = argparse.ArgumentParser(
    description='This program prints a color HEX value'
)

parser.add_argument('-c', '--color', metavar='color', required=True,
                    choices={'red', 'yellow'},
                    help='the color to search for')

args = parser.parse_args()

print(args.color)  # 'red'



