# Write some code that determines and prints whether the number 3 
# appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

def numbers(number_set):
    value = 3 in number_set
    print(value)
numbers(numbers1)             # True
numbers(numbers2)             # False
numbers(numbers3)             # False
numbers(numbers4)             # False
numbers(numbers5)             # True

# Launch School Answer:
print(3 in numbers1)          # True
print(3 in numbers2)          # False
print(3 in numbers3)          # False
print(3 in numbers4)          # False (3 != '3')
print(3 in numbers5)          # True  (3 == 3.0)