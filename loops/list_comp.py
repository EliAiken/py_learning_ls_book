squares = [ number * number for number in range(5) ]
print(squares)      # [0, 1, 4, 9, 16]

multiples_of_6 = [ number for number in range(20)
                   if number % 6 == 0 ]
print(multiples_of_6)      # [0, 6, 12, 18]

even_squares = [ number * number
                 for number in range(10)
                 if number % 2 == 0 ]
print(even_squares)      # [0, 4, 16, 36, 64]

print()

cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

names = [ name.upper() for name in cats_colors ]
print(names)
names = [ name.upper() for name in cats_colors.values()]
print(names)
# ['TESS', 'LEO', 'FLUFFY', 'BEN', 'KAT']
# ['BROWN', 'ORANGE', 'GRAY', 'BLACK', 'ORANGE']

names = [ name.upper()
          for name in cats_colors
          if cats_colors[name] == 'orange' ]
print(names)