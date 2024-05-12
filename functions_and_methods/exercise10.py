# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# First guess: foo() will print 3 objects: 42, 3.141592, and 2 as there
# was no 3rd argument passed to the 3rd parameter in the function, thus calling
# the default value to be used instead, which prints 2.

# Launch School answer: Here, we've defined foo with three parameters, 
# with the second and third parameters having default values. We've 
# passed the function two arguments, so Python uses the default value 
# for the last argument.

