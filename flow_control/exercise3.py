# Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)


# First Guess: the code will print 'Product 2' and 'Product not found!'
# due to the case '113' being called in the first expression and the 
# case _ being called in the second expression.

# Launch School answer: The first call to bar_code_scanner prints Product2 
# since the first case that matches '113' is the one on line 5. The second 
# call prints Product not found! since the numeric value 142 doesn't match 
# any of the case statements with string arguments. Instead, it matches the
#  _ "default" case.