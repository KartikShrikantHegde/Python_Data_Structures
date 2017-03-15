# import sys
#
# def find_duplicate(my_arr):
#     visited_arr = [False] * (2**20)
#
#     for i in range(0,len(my_arr)):
#         if visited_arr[my_arr[i]]:
#             return my_arr[i]
#
#         visited_arr[my_arr[i]] = True
#
#     return -1
#
# print find_duplicate(my_arr=[10, 20, 30, 40, 40,20])


# nums = [2,14,18,22,22]
#
# print len(nums), len(set(nums))
# print len(nums) != len(set(nums))


from collections import Counter
mylist = [20, 30, 25, 20]
for k,v in Counter(mylist).items():
    if v > 1:
        print k