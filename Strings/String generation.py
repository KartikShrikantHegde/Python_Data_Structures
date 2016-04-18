print ''.join([`x` for x in xrange(101)])

#Or

my_list = list()
for x in range(101):
    my_list.append(`x`)

print ''.join(my_list)