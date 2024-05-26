# Which of the following values can't be used as a key in a dict object, and why?

# 'cat'                                     # Yes
# (3, 1, 4, 1, 5, 9, 2)                     # Yes
# ['a', 'b']                                # No, List
# {'a': 1, 'b': 2}                          # No, Dict
# range(5)                                  # Yes
# {1, 4, 9, 16, 25}                         # No, Set
# 3                                         # Yes
# 0.0                                       # Yes
# frozenset({1, 4, 9, 16, 25})              # Yes

# The above items cannot be used as keys in dict objects because they are mutable
# and non-hashable objects. --> The rest are immutable, built-in objects so they
# can be used as dict keys.