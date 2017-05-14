''' Recursive Fibonacci '''

def recursive_fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return recursive_fib(n-1) + recursive_fib(n-2)

print recursive_fib(6)


''' Iterative fibonacci '''


# def fib_iterative(n):
#     a = 0
#     b = 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a
#
# print fib_iterative(0)

