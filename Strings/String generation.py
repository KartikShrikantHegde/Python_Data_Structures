# print ''.join([`x` for x in xrange(10)])

#Or
x = [1,2,3]
print str(x)
my_list = list()
for x in range(10):
    my_list.append(`x`)
print my_list

print '-'.join(my_list)
print list(my_list)