def is_empty_or_blank(string):
    if string.isspace():
        return True
    elif string:
        return False
    else:
        return True

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

# def is_empty_or_blank(str):
#     return not str or str.isspace()

# print(is_empty_or_blank('mars'))
# print(is_empty_or_blank('  '))
# print(is_empty_or_blank(''))