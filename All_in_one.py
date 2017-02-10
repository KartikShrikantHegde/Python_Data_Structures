# # # Built in data types are mainly - int and float in python
# # # Then there are others like bool etc..
# #
# # # -----------------------------------------------------------------------
# #
# # # These are python collection data types or data structures
# # #
# # # Ordered collections are - list, tuples, strings
# List and Tuple - Contain objects
# Strings contain characters
# # # because they have certain order of arrangement in memory and we can access them using indexes
# #
# # # Strings are immutable
# #
# # # Even when concatenated original string remains unchanged
# #
# # my_str = "Karthik"
# # my_str = my_str + " H"
# #
# # print my_str
# #
# # # Accessing string value using indexes
# # print my_str[0]
# # print my_str[7]
# #
# # # Immutable
# #
# # my_str[0] = "J"
# # print my_str[0]
# #
# # # Tuples are immutable
# # Tuples can have duplicate values though
# my_tuple = (4,5,6,6)

# Another way of creating tuples is to simply put elements using comma seperated
#
# my_new_tuple = 5,6,6,[1,2,3]
# print my_new_tuple
# print my_new_tuple                 -> (5,6,6,[1,2,3])
#
# Immutable
# my_tuple[1]= "Hi"
#
# # adding elements is possible even though they are immutable and values should not be added to existing
# # tuple without creating a new tuple
#
# my_tuple = my_tuple + (7,8)
# print my_tuple
#
# # accessing tuple values using indexes
# print my_tuple[0]
#
# # Arrays are mutable - both adding and changing possible
#
# # my_arr = [10,20,30]
# # my_arr[0] = 50
# # my_arr.append(60)
# #
# # print my_arr
#

# Unordered Collections are - sets and dict

# Sets - are mutable, i.e adding an element is possible to existing set, even though you cant modify existing element
# in sets as it cant be accessed through indexing

# Sets internally use hashing of each element so that they can be stored uniquely without duplicates

# Declaring set with values

# my_set = {1,2,3}

# Note: my_set = {}   -> this is a dict, not a set

# Adding element is possible but no duplicates are allowed.
# my_set.add(3)
# print my_set

# my_set.add(4)
# print my_set

# Using set keyword on list

# l = [1, 2, 3, 3]
# s = set(l)
# print s

# Note : you cant use indexing on sets -> print s[0] is error

# # Frozensets - used to get immutable sets
# frozen = frozenset([1, 2, 3])
# frozen.add not possible as its immutable

# Dictionary -> Unordered collection
# keys are immutable but values are mutable
#
# vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5:'u'}
#
# vowels[2] = "m"
#
# vowels[6] = "Karthik"
#
# vowels.update({7:"Hegde"})
#
# print vowels
#
# d = dict()
#
# d['a'] = 10
# d['b'] = 20
#
# for (key,value) in d.items():
#     print key,value
#
#
# #####################################
#
# m = {}
#
# m['a'] = 'alpha'
# m['g'] = 'gamma'
# m['o'] = 'omega'
#
# print m
#
# print m.keys()
# print m.values()
#
# # This returns list of tuple pairs
#
# print m.items()

# Counter and Enumerate

elements = ['foo', 'bar', 'baz']

for count, elem in enumerate(elements):
    print count, elem
from collections import Counter

my_element = [1,2,3,4,2]

for key,value in Counter(my_element).items():
    print key,value




