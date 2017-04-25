# Generators:
#
# Generators are iterators, but you can only iterate over them once. It's because they do not store all the values in memory, they generate the values on the fly:
#
# >>> mygenerator = (x*x for x in range(3))
# >>> for i in mygenerator:
# ...    print(i)
# 0
# 1
# 4
# It is just the same except you used () instead of []. BUT, you cannot perform for i in mygenerator a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.


def gen(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

print gen(10)

# Generators yield more than the return