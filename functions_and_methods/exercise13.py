# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# First guess: when invoked, this function will throw an error due to
# having no 3rd default value attached to the 3rd parameter in the
# function definition. A function has to give a default value to every
# subsequent parameter after one default value has been assigned. So in
# this instance, the 2nd parameter was given a default value which would
# obligate the 3rd parameter to also have a default value assigned to it.

# Launch School answer: Here, we've defined foo with three parameters, 
# with the second parameter having a default value. This is an error, 
# however. Once Python sees a positional parameter with a default value, 
# all subsequent parameters must have default values.

# SyntaxError: non-default argument follows default argument