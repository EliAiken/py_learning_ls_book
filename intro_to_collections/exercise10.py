# Bob expects the following code to print the names in 
# alphabetical order. Without running the code, can you 
# say whether it will? Explain your answer.

names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)

# First Guess: This will not print in alphabetical order
# because it is a set and sets are unordered collections,
# meaning that their contents may print in an order other
# than their originally inputed order.

# Launch School Answer: This code probably won't print the 
# names alphabetically. Sets, by definition, are unordered 
# collections. Thus, the order in which members are shown when 
# printing or iterating is arbitrary. Bob's code may print 
# the names alphabetically on rare occasions, but it would do 
# so only once every 5040 times.