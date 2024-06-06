def first_planet(lst):
    if lst:
        return lst[0]
    else:
        return None

print(first_planet(['Earth', 'Moon', 'Mars']))  # Earth
print(first_planet([]))