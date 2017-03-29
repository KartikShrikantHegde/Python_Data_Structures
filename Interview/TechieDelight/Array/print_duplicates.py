import sys

def find_duplicate(my_arr):
    visited_arr = [False] * 256

    for i in range(0,len(my_arr)):
        if visited_arr[ord(my_arr[i])]:
            print my_arr[i]

        visited_arr[ord(my_arr[i])] = True

print find_duplicate(my_arr='Kansas')


# nums = [2,14,18,22,22]
#
# print len(nums), len(set(nums))
# print len(nums) != len(set(nums))

#
# from collections import Counter
# mylist = [20, 30, 25, 20]
# for k,v in Counter(mylist).items():
#     if v > 1:
#         print k