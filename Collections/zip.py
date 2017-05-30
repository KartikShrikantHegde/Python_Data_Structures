# # pascal triagle
# #
# # class Solution(object):
# #     def getRow(self, rowIndex):
# #         """
# #         :type rowIndex: int
# #         :rtype: List[int]
# #         """
# #         row = [1]
# #         for _ in range(rowIndex):
# #             row = [x + y for x, y in zip([0]+row, row+[0])]
# #         return row
# #
# #     --------------------------------
# #
# #     class Solution:
# #         # @return a string
# #         def longestCommonPrefix(self, strs):
# #             if not strs:
# #                 return ""
# #
# #             for i, letter_group in enumerate(zip(*strs)):
# #                 if len(set(letter_group)) > 1:
# #                     return strs[0][:i]
# #             else:
# #                 return min(strs)
#
#
# # This function takes two equal-length collections,
# # and merges them together in pairs. if one of the collection has more len that
# # extra len val is ignored for mapping
# #
# # It can merge 2 tuples or lists or dicts but returns list of tuples grouped together
#
# # here key 9 is ignored as its an extra len of 2 lists
#
# # x = {1:'x', 2:'y', 3:'z',9:"v"}
# # y = {4:"z", 5:"a", 6:"q"}
# # print zip(x, y)
# #
# # x = [1,2]
# # z = ['s','x']
# #
# # # m = (1,2,3)
# # # n = (4,5)
# #
# # print zip(x,z)
# #
# # mycoll = [x for x in range(2,6,-1)]
# # print mycoll
# #
# # t = [0,1]
# # a, = t
# #
# # print a ,t
#
# # def f(func):
# #     def g(param):
# #         return "!{0}!".format(func(param))
# #     return g
# # @f
# # def h(something):
# #     return "...{0}...".format(something)
# # print h("john")
#
# # def f(x,*y,**z):
# #     print z
# # f(1,2,3)
#
# # from functools import partial
# #
# # f = partial(range,5,10)
# # print f(2)
#
# # def f(val,de=[]):
# #     de.append(val*2)
# #     print de
# #
# # f("f")
# # f("s",de=["some","test"])
# # f("t")
#
# class Myclass():
#     def __call__(x):
#         yield x
#

# print Myclass()(3)

# -------------------------------
# x =  [[] for x in range(3)]
# x[0].append(10)
# print x
# -------------------------------







# business = [{'100':500},{'100':400,},{'100':500},{'100':300,},{'100':900},{'100':400,}]
#
# newlist = sorted(business, key=lambda k: k['100'])
#
# print newlist

# dct = {'a': 5, 'c': 7, 'b': 2, 'e': 5, 'd': 5}
# print sorted(dct, key=lambda k: (-dct[k], k))

# dct = {'a': 5, 'c': 7, 'b': 2, 'e': 5, 'd': 5}
# my_list = list()
#
# for key,value in dct.items():
#     my_list.append((value,key))
#
# my_list.sort()
# print my_list

#
# from collections import OrderedDict
# my_dict = {1:['1', '2', '3'], 4: ['5', '6', '7'], 2: ['10', '11']}
#
# new_dict = OrderedDict((k, v) for k, v in sorted(my_dict.items(), key=lambda x: x[0]))
# print(new_dict)

# dct = {'a': 5, 'c': 7, 'b': 2, 'e': 5, 'd': 5}
# my_list = list()
#
# for key,value in dct.items():
#     my_list.append((value,key))
#
# print my_list
# print dict(my_list)

# a = [{"x": 200, "y": 1000},
#      {"x": 201, "y": 900}
#      ]

#
# colour = {'blue': 5, 'purple': 6, 'green': 2, 'red': 2}
# min_val = min(colour.itervalues())
#
# print min_val
# # [k for k, v in colour.iteritems() if v == min_val]
# # ['green', 'red']

def findRestaurant(list1, list2):
     """
     :type list1: List[str]
     :type list2: List[str]
     :rtype: List[str]
     """
     d = {}

     for i in xrange(len(list1)):
          d[list1[i]] = i

     final_dict = {}
     for j in xrange(len(list2)):
          if list2[j] in d.keys():
               final_dict[list2[j]] = j + d[list2[j]]

     min_val = min(final_dict.itervalues())
     print min_val

     return [key for key, value in final_dict.iteritems() if value == min_val]

print findRestaurant(list1=["Shogun","Tapioca Express","Burger King","KFC"],list2=["KFC","Shogun","Burger King"])





