# Both of them perform the same functions

# Xrange is -> Generator
# It doesnt allocate all the values in memory that you want to loop through
# Thus best when a loop of large val to be iterated

for i in xrange(0,10000):
    pass


# range -> Allocates values in memory as list for the range specified.lambda
# thus range(1000) means internally it creates 1000 values in memory for looping
# Not Good for large value of looping.

for x in range(10):
    pass