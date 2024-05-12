# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# First guess: this will throw an error because the function only has
# 2 parameters, but 3 arguments were passed to the function.

# Launch School answer: We've defined foo with two parameters. However, 
# we've passed the function three arguments. This is an error.
#TypeError: foo() takes 2 positional arguments, but 3 were given