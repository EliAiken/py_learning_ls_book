def compare_by_length(word1, word2):
    if len(word1) < len(word2):
        print(-1)                           # return -1 for problem requirement
    elif len(word1) > len(word2):
        print(1)                            # return 1 for problem requirement
    else:
        print(0)                            # return 0 for problem requirement


compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0