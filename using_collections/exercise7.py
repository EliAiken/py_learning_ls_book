# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
parts = info.split(':')
result = '+'.join(parts)
print(result)

# Another way to do this with the str.replace function -->
# info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
# result = info.replace(':', '+')
# print(result)                     # Prints original string with ':' replaced with '+'