# Write a function that computes and returns the factorial 
# of a number by using a for or while loop. The factorial 
# of a positive integer n, signified by n!, is defined as 
# the product of all integers between 1 and n, inclusive:

def factorial(n):
    result = 1
    for number in range(n, 0, -1):      # could also be written range(1, n + 1)
        result *= number
        
    return result

print(factorial(25))


def factorial(n):
    result = 1
    while n > 0:
        result *= n     # result = result * n
        n -= 1          # n assigned to the current value of n - 1

    return result