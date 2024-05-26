# We'll return to the simpler one-dimensional version of my_list. 
# In this problem, you should write code that creates a new list 
# with one element for each number in my_list. If the original number 
# is an even, then the corresponding element in the new list should 
# contain the string 'even'; otherwise, the element should contain 'odd'.

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

result = []
for number in my_list:
    if number % 2 == 0:
        result.append('even')
    else:
        result.append('odd')
print(result)

result1 = [ 'even' if number % 2 == 0 else 'odd'
           for number in my_list ]
print(result1)