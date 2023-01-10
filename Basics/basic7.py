# args vs kwargs


# *args: Python makes a tuple of these arguments with the name we use after the asterisk(*) 
# and makes this variable available to us inside the function. This asterisk(*) is called an 
# “unpacking operator”.
def product(*numbers):
    
    prod = 1
    for n in numbers:
        prod *= n
    return prod

print(product(2,3,4))
print(product(2,2))


# **kwargs: it allows us to pass the variable length of keyword arguments to the function.
def whatTechTheyUse(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append("{} uses {}".format(key, value))
    return result
 
print(whatTechTheyUse(Google='Angular', Facebook='react', Microsoft='.NET'))
