print('johnson' in 'Joe Johnson')               # False; case sensitive
print('sen' not in 'Joe Johnson')               # True
print('Joe J' in 'Joe Johnson')                 # True
print(5 in range(5))                            # False; only goes from 0 to 4
print(5 in range(6))                            # True
print(5 not in range(5, 10))                    # False
print(0 in range(10, 0, -1))                    # False
print(4 in {6, 5, 4, 3, 2, 1})                  # True
print({1, 2, 3} in {1, 2, 3})                   # False
print({3, 2} in {1, frozenset({2, 3})})         # True

# Without running the above code, determine what each line should print.

# in and not in reference value equality, not object equality
# what this means is that is the value on the left side of in/not in the
# same value as the item on the right side?

# example: print([1] in [1, 2, [1]]) --> True; list value is located within other list
#          print([1] == [1]) --> True; same values
#          print([1] is [1]) --> False; same values, different objects