# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# First guess: the function will print 3 objects: 42, 3, and 2 as 
# there was only 1 argument passed to the function, however the 
# function had 3 parameters, the last two of which had default values
# to use. Thus, the default values of the 2nd and 3rd parameter will
# be used for this call to foo().

# Launch School answer: Here, we've defined foo with three parameters, 
# with the second and third parameters having a default value. We've 
# passed the function one argument, so Python uses the default value 
# for the last two parameters.

