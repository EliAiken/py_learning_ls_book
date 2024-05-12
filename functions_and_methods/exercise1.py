# What happens when you run the following program? 
# Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# Results in 'foo' not defined b/c foo was initialized
# inside the scope of the defined function level and the call
# to print foo on line 8 was in the global scope. Foo was 
# not found in the global scope and thus could not be 
# printed when called in line 8.