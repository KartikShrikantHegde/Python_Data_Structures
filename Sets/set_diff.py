# The resulting set has elements of the left-hand set with
# all elements from the right-hand set removed.
# An element will be in the result if it is in the left-hand set and not in the right-hand set.


fib = set((1, 1, 2, 3, 5, 8, 13, 11, 19))

prime = set((2, 3, 5, 7, 11, 13))

print fib - prime

# set([8, 1])
