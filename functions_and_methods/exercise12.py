# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# First guess: python will throw an error because foo() requires at least
# one argument to be passed to the parameter as per the definition of the
# function. Thus, making an error occur which will probably say something 
# like "needs at least 1 argument". If the 1st parameter had a default value
# attached to it, then this would have printed the default values attached to
# all 3 parameters in the function.

# Launch School answer: Here, we've defined foo with three parameters, 
# with the second and third parameters having default values. We haven't 
# passed the function any arguments. That's an error, though - the 
# first parameter has no default value.
# TypeError: foo() missing 1 required positional argument: 'first'