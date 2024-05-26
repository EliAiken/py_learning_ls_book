# The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:          # This expression will only stop when it evaluates as falsy
    print(counter)          # This will always be less than 5 (truthy), so it never stops

# First Guess: This causes an infinite loop because there is only 1 iteration for
# the block before it ends and will not keep counting up to 5. This means that 0 
# will print forever unless we added something like:

    counter += 1

# To the end of the code block

# Launch School Answer: The problem occurs in the loop body. We never increment 
# counter, so counter < 5 always returns a truthy value.