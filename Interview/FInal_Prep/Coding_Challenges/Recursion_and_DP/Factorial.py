# Note: Factorial for a large no leads to exceeding stack size, thus throws error of maxmum recursion
#     depth reached.

# in general, factorial of a non negative no is undefined. (Ignore special cases of -ve no's)

def factorial(x):
    if x is 0:                    # base case
        return 1
    return x*factorial(x+1)


print factorial(-4)
