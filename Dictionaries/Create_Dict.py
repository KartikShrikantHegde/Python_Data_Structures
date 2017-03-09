# Dictionary -> Unordered collection
# keys are immutable but values are mutable

# a Python dictionary throws a KeyError
# if you try to get an item with a key that is not currently in the dictionary.

vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5:'u'}

vowels[2] = "m"

vowels[6] = "Karthik"

vowels.update({7:"Hegde"})

print vowels

d = dict()

d['a'] = 10
d['b'] = 20

for (key,value) in d.items():
    print key,value


#####################################

m = {}

m['a'] = 'alpha'
m['g'] = 'gamma'
m['o'] = 'omega'

print m

print m.keys()
print m.values()

# This returns list with key value as tuples

print m.items()


# Its not sorted

import collections

print 'Regular dictionary:'
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v




