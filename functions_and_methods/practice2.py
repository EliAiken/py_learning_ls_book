my_str = 'abc-123-def'
print(my_str.upper())   # Method call

#   #   #   #   #   #   #   #   #   #   #   #   #   #

my_list = [1, 2, 3, 4]
my_list.pop()           # Mutate argument
print(my_list)

def add_number(my_list):
    my_list.append(5)   # Mutate argument

add_number(my_list)
print(my_list)