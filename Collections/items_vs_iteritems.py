# Use iteritems() to iterate over large dictionary because,
# it returns an iterator object to traverse and print the key,values
# Thus it takes less space.
# Note : Iterator is called as Generator just like xrange

# items() -> returns a copy of each of key,val of the dict.
# Thus takes a lot of memory and not good for large dict

# -----------------------------------------------------------------

# Both of them perform same functionality


my_list = {1:"abc", 2:"text", 3:"dfsd"}

for k, v in my_list.items():
    print k, v

for k, v in my_list.iteritems():
    print k, v