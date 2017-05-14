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

The difference between shallow and deep copying is only relevant for
compound objects, which are objects containing other objects, like lists or class instances.

For immutable objects, there is no need for copying because the data will never change, so Python uses the same data; ids are always the same. For mutable objects, since they can potentially change, [shallow] copy creates a new object.

Deep copy is related to nested structures. If you have list of lists, then deepcopy copies the nested lists also, so it is a recursive copy. With just copy, you have a new outer list, but inner lists are references.

Assignment does not copy. It simply sets the reference to the old data. So you need copy to create a new list with the same contents.



import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

Using normal assignment operatings to copy:

d = c

print id(c) == id(d)          # True - d is the same object as c
print id(c[0]) == id(d[0])    # True - d[0] is the same object as c[0]
Using a shallow copy:

d = copy.copy(c)

print id(c) == id(d)          # False - d is now a new object
print id(c[0]) == id(d[0])    # True - d[0] is the same object as c[0]
Using a deep copy:

d = copy.deepcopy(c)

print id(c) == id(d)          # False - d is now a new object
print id(c[0]) == id(d[0])    # False - d[0] is now a new object


--------------------------------------------------------------------------



# Shallow copying

import copy

a = {'x': [1], 'y': 2, 'z': 4}

b = a.copy()

# Both have the same values

print id(a),id(b)

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
