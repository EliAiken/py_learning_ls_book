import random
random_number = random.randint(0, 1)

print('Yes!') if random_number == 1 else print('No!')
print('Yes!' if random_number else 'No!')

# if random_number == 1:
#     print('Yes!')
# else:
#     print('No!')


# Ternary Expression:       expression1 if condition else expression2