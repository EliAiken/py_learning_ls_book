# Without running this code, what will it print? Why?

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)                     # Makes new dictionary object, which means it isn't the same object as dict1
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])