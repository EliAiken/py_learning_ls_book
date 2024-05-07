# Question 1

# Concatenate two strings, one with your first 
# name and one with your last, to create a new string 
# with your full name as its value. For example, if 
# your name is John Doe, you should combine 'John' 
# and 'Doe' to get 'John Doe'.

name = 'Eli' + ' Aiken'
print(name)

# Question 2
# Use the REPL and the arithmetic operators to extract the individual digits of 4936
n = 4936
a = n // 10
b = a // 10
c = b // 10
print(c % 10, b % 10, a % 10, n % 10)

# Question 3
# What does the following code do?

print('5' + '10')   # This concatenates the strings and makes 510, not 15

# Question 4
# Refactor the code from the previous exercise to use coercion to print 15 instead

print(int('5') + int('10'))

# Question 5
# Yes --> error 'list index out of range'

# Question 6
# To what value does the following expression evaluate?

'foo' == 'Foo'      # False --> 'f' != 'F'
'foo' > 'Foo'       # True --> any lowercase letter is greater than any uppercase letter

# Question 7
# What will the following code do? Why?

int('3.1415')       # Raises ValueError; str must be reassigned to float, then passed with
                    # int(float) function

# Question 8
# To what value does the following expression evaluate?

'12' < '9'          # True since strings --> compare 1 character at a time
                    # '1' < '9' so '12 is < '9'
                    # False if integers --> 2 integer places is greater than 1 always


