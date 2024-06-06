grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

while grocery_list:
    checked_item = grocery_list.pop(0)
    print(checked_item)

print(grocery_list)

            # Alternate solution #
            
# grocery_list = list(reversed(grocery_list))
# while len(grocery_list) > 0:
#     print(grocery_list.pop())

# print(grocery_list)