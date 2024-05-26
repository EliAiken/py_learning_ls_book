# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# This code is going to print the first line at value 8 because we sliced
# the string before calling .rfind, which means that we will use a new
# sliced string when finding the appropriate index for the arguments given. 
# We begin the search at index 21 and will stop at index 35 exclusive,
# however with .rfind, the function will work right to left instead of 
# left to right. This will put the 'f' character at index 8 for this
# sliced string.

# The second snippet of code will print value 29 because we did NOT slice
# the string before calling the .rfind function, thus we did not create a new
# string, but rather we are referring to the original. This will put the first
# 'f' character, searched from right to left, at index 29.