name = 'Roger'

if name.casefold() == 'RoGeR'.casefold():
    print(True)
else:
    print(False)

if name.casefold() == 'DAVE'.casefold():
    print(True)
else:
    print(False)

# print(True if name.casefold() == 'RoGeR'.casefold() else False)
# print(True if name.casefold() == 'DAVE'.casefold() else False)