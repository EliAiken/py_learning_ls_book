# Write a function that takes a string as an argument and 
# returns an all-caps version of the string when the string 
# is longer than 10 characters. Otherwise, it should return 
# the original string. Example: change 'hello world' to 
# 'HELLO WORLD', but don't change 'goodbye'.

def string_caps(my_string):
    if len(my_string) > 10:
        print(my_string.upper())
    else:
        print(my_string)

my_string = input('Enter a phrase: ')
string_caps(my_string)

# Launch School answer:

def caps_long(string):          # Uses return function, then prints after passing
    if len(string) > 10:        # arguments to parameters (lines 24-27)
        return string.upper()
    else:
        return string

print(caps_long("Sue Smith"))     # Sue Smith
print(caps_long("Sue Roberts"))   # SUE ROBERTS
print(caps_long("Joe Shea"))      # Joe Shea
print(caps_long("Joe Stevens"))   # JOE STEVENS