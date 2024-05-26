# What will the following code print?

print('abc-def'.isalpha())                  # False; dash
print('abc_def'.isalpha())                  # False; underscore
print('abc def'.isalpha())                  # False; space in between strings

print('abc def'.isalpha() and               # False; both false
      'abc def'.isspace())

print('abc def'.isalpha() or                # False; both false
      'abc def'.isspace())

print('abcdef'.isalpha())                   # True
print('31415'.isdigit())                    # True
print('-31415'.isdigit())                   # False; - sign
print('31_415'.isdigit())                   # False; underscore
print('3.1415'.isdigit())                   # False; . is not a digit
print(''.isspace())                         # False; empty string, not space