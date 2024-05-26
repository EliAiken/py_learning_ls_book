names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name == 'Max':
        continue

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names);
# ['CHRIS', 'KARIS', 'VICTOR']

names = ['Chris', 'Max', 'Karis', 'Victor']             # Same outcomes as solution above
upper_names = []

for name in names:
    if name != 'Max':
        upper_name = name.upper()
        upper_names.append(upper_name)

print(upper_names);
# ['CHRIS', 'KARIS', 'VICTOR']