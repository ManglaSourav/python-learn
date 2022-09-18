'''
Closures
If you return a nested function from a function, that nested function
has access to the variables defined in that function, even if that 
function is not active any more.
'''


def counter():
    '''sample doctring'''
    count = 0

    def increment():
        # The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
        nonlocal count
        count = count + 1
        return count

    return increment


increment = counter()

print(increment())  # 1
print(increment())  # 2
print(increment())  # 3


'''
Decorators
Decorators are a way to change, enhance or alter in any way how a function works.
Decorators are defined with the @ symbol followed by the decorator name, just before the function definition.
A decorator is a function that takes a function as a parameter, wraps the function in an inner function 
that performs the job it has to do, and returns that inner function. In other words:
'''


def logtime(func):
    # The purpose of having a wrapper function is that a function decorator receives a function
    # object to decorate, and it must return the decorated function.
    def wrapper():
        # do something before
        val = func()
        # do something after
        return val
    return wrapper


@logtime
def hello():
    print('hello!')


hello()


# function returing function
def create_adder(x):
    def adder(y):
        return x+y

    return adder


add_15 = create_adder(15)(10)
print(add_15)


# print doctstring/ comments of a function(# comments dont work only "or' will work)
# print(print.__doc__)
print(counter.__doc__)
