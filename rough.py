# # def binary_search(lowerLimits,upperLimits,scores):
# #     final = [0] * len(lowerLimits)
# #     for i in range(len(scores)):
# #         for x in range(len(lowerLimits)):
# #             if scores[i] >= lowerLimits[x] and scores[i] <= upperLimits[x]:
# #                 final[x] += 1
# #     return final
# #
# # lower_arr = [2]
# # higher_arr = [6]
# # scores = [3,5,6]
# # print binary_search(lower_arr,higher_arr,scores)
# #
# #
# # #
# # #
# # # lower_arr = [1,2]
# # # higher_arr = [4,5]
# # # scores = [2,2,2,4,5]
# # # print binary_search(lower_arr,higher_arr,scores)
# # #
# # #
# # # def binary_search(scores,lowerLimits,upperLimits,scores):
# # #
# # #     temp = []
# # #     from collections import Counter
# # #     counter = Counter(scores)
# # #
# # #     for i in range(0,len(lowerLimits)):
# # #         low = lowerLimits[i]
# # #         high = upperLimits[i]
# # #         val = 0
# # #         for key in counter.keys():
# # #             if low <= key <= high:
# # #                 val = val + counter[key]
# # #         temp.append(val)
# # #
# # #     return temp
# #
# #
#
# def dutchNationalFlag(A, piv):
#     assert 0 <= piv <= len(A) - 1
#     if len(A) == 0:
#         return A
#     else:
#         low = 0
#         mid = 0
#         high = len(A) - 1
#         pivot = piv
#
#         while mid <= high:
#             if A[mid] < A[pivot]:
#                 A[mid], A[low] = A[low], A[mid]
#                 low += 1
#                 mid += 1
#             elif A[mid] == A[pivot]:
#                 mid += 1
#             elif A[mid] > A[pivot]:
#                 A[mid], A[high] = A[high], A[mid]
#                 high -= 1
#
#         return A
#


#
# nums = [1,0,2,0,2,1,1]
# print dutchNationalFlag(nums,4)


# my_arr = [1,0,2,0,2,1,1]
# smaller = [1,0,0,1,1]
# pivot = [2]
# larget = [2]
#
# my_arr[:] = smaller[0:] + pivot + larget[0:]
# print my_arr
#
# my_arr = [3,1,4,1,3,5,4]
# from collections import Counter
# print type(Counter(my_arr))




# class Sample(object):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#
# sam = Sample(10,20)
# sam.x = 25
# sam.y = 50
#
# new_obj = sam
# sam.x = 100
# sam.y = 200
#
# new_obj.x = 500
# new_obj.y = 1000
#
# print new_obj is sam
# print new_obj == sam
# print sam,new_obj
#
# print new_obj.x, new_obj.y
# print sam.x, sam.y

#
# l = [5,2,3,[11,20,30]]
#
# l1 = list(l)
#
# print l , l1
#
# l[0] = 7
# l1[0] = 9
#
# l1[3][0] = 50
#
# print l , l1

# s = "abc"
#
# x = list(s)
#
# print s,x

import copy

a='deepak'
b=1,2,3,4
c=[1,2,3,4]
d={1:10,2:20,3:30}

print a,b,c,d