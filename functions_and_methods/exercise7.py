# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# First guess: this will throw an error because we did not provide
# 2 different arguments to the foo() function, thus causing Python 
# to run an error because there were 2 parameters to be met.

# Launch School answer: We've defined foo with two parameters. 
# However, we've only passed it one argument. This is an error.
# TypeError: foo() missing 1 required positional argument: 'qux'
