# Write Python code to print the seventh number of range(0, 25, 3).

seventh = range(0, 25, 3)
print(list(seventh))

print(list(seventh[6:7]))   # This was my answer, it printed the index 7, not seventh number

print(seventh[6])           # Correct answer