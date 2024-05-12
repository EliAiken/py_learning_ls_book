def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# This code does not print anything because the `return` on line
# 3 terminates the function invocation before it can print anything.
# Returns `None` by default