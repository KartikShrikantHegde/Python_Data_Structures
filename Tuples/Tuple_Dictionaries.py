# Tuple and dictionaries
# Take a dictionary and convert into list of tuples

d = dict ()

d['a'] = 10
d['b'] = 20

for (key,value) in d.items():
    print key,value


my_tuple = d.items()

print my_tuple