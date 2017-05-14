# This syntax is a slice assignment. A slice of [:] means the entire list. The difference between nums[:] = and nums = is that the latter doesn't replace elements in the original list. This is observable when there are two references to the list
#
# >>> a = list(range(10))
# >>> b = a
# >>> a[:] = [0, 0, 0] # changes when a and b both refer to
# >>> b
# [0, 0, 0]
# To see the difference just remove the [:] from the above sequence.
#
# >>> a = list(range(10))
# >>> b = a
# >>> a = [0, 0, 0] # a now refers to a different list than b
# >>> b
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list1 = ['a','b','c','d']
# list2 = list1[:]
#
# print id(list1), id(list2)

# colours1 = ["red", "green"]
# colours2 = colours1
# print id(colours1),id(colours2)
# print colours1, colours2
# colours1[0] = "Yellow"
# print colours1, colours2
# print id(colours1),id(colours2)
# print
# print '--------------------------------------'
# print
# colours1 = ["red", "green"]
# colours2 = colours1
# print id(colours1),id(colours2)
# print colours1, colours2
# colours1 = ["Blue"]
# print colours1, colours2
# print id(colours1),id(colours2)
#


#
# colors1 = ["voilet","pink"]
# colors2 = colors1
# colors1[:] = [0,0,0]
# print colors1, colors2
# print id(colors1), id(colors2)
#
#
# # print '--------------------------------------'
# # print
# #
# colors1 = ["voilet","pink"]
# colors2 = colors1[:]
# print colors1, colors2
# print id(colors1), id(colors2)
#
# colors1[0] = "XXX"
# print colors1, colors2
#
# colors1 = ["voilet","pink"]
# colors2 = colors1[:]
# colors1 = [0,0,0]
# print colors1, colors2
# print id(colors1), id(colors2)
#
#
#
# print '--------------------------------------'
# print

import copy
#
# man = ['x','y']
# woman = copy.copy(man)
#
# print id(man),id(woman)
# print man, woman
# man[0] = 'p'
# print man,woman
#
# man = ['x','y']
# woman = copy.copy(man)
#
# print id(man),id(woman)
# print man, woman
# man = ['s','t']
# print man,woman

d = copy.deepcopy(c)

print id(c) == id(d)          # False - d is now a new object
print id(c[0]) == id(d[0])    # False - d[0] is now a new object


a1 = a[:]
print a,a1
a1[0] = "Orange"

print a1 , a
print id(a),id(a1)