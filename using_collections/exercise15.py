pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
values = pets.values()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)                     # dict_keys(['Cat', 'Bird', 'Snake'])
print(values)                   # dict_values(['Meow', 'Tweet', 'Sssss'])

# Without running the code, what values will be printed by line 10?