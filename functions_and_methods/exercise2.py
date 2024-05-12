# Take a look at this code snippet: What does this program print? Why?

foo = 'bar'

def set_foo():
    foo = 'qux'     # This foo is within the function level scope
                    # and is intializing the variable to 'qux' in
                    # this example. This variable only exists at 
                    # the function level, not the global level and
                    # thus will not be called when invoked in line 13.

set_foo()
print(foo)          # This will print 'bar' as it was globally scoped
                    # in line 3 and it is called in the function on 
                    # line 13 to print. 

