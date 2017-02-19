print ''.join([`x` for x in xrange(10)])

#Or

my_list = list()
for x in range(10):
    my_list.append(`x`)

print ''.join(my_list)