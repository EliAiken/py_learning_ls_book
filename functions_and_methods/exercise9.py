# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# First guess: function foo will print 3 objects, 42, 3.141592, and 2.718.
# This is because the function foo() has 3 parameters with 2 of them being
# default parameters, however there were 3 arguments passed to the 3 parameters
# and thus none of the default parameters will take effect. This will then
# print the 3 passed arguments to the function.

# Launch School answer: Here, we've defined foo with three parameters, 
# with the second and third parameters having default values. However, 
# we've passed all three arguments to the function, so Python ignores 
# the default values.

