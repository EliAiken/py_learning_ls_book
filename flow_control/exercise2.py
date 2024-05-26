# Write a function, even_or_odd, that determines whether 
# its argument is an even or odd number. If it's even, the 
# function should print 'even'; otherwise, it should print 
# 'odd'. Assume the argument is always an integer.

def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')
number = int(input('Enter a number: '))
even_or_odd(number)


# Another way to write this as a ternary expression:

# def even_or_odd(number):
#   print('even' if number % 2 == 0 else 'odd')

# Ternary Expression 'Formula': <expression1 if condition else expression2>