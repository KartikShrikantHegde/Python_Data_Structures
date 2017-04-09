# in Python you can use copy() to copy the object
#
# 2 ways -> 1. Shallow copying
#             This is same as pass by object. both the original object and
#             copied object point to the same box. Thus any changes to original box updates the
#             copied object as well.
#
#           2. Deep copying:
#             This is like pass by value. The original object and copied object
#             both have their own copies of values. Therefore any changes to one
#             doesnt alter other one.
#
#
#
#
#

# Shallow copying

import copy

a = {'x': [1], 'y': 2, 'z': 4}

b = a.copy()

# Both have the same values

print a,b

a['x'].append(2)

# Both have same values
print a, b

# Both have same values
b['x'].append(5)
print a, b



print '----------------------------------------------------------------'

# Deep copying

a = {'x': [1], 'y': 2, 'z': 4}

b = copy.deepcopy(a)

# Both are same now

print a, b

# a value changes but doesnt affect b
a['x'].append(2)

print a, b

# Changing b value. but doesnt affect a

b['x'].append(5)

print a,b
