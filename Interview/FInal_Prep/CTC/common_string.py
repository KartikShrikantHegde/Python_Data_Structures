import sys


def minimum(arr1,arr2):
    my_dict = {}

    for i in range(len(arr1)):
        if arr1[i] not in my_dict.keys():
            my_dict[arr1[i]] = i

    min = sys.maxint
    my_str = ''
    for i in range(len(arr2)):
        if arr2[i] in my_dict.keys() and i + my_dict[arr2[i]] < min :
            min = i + my_dict[arr2[i]]
            my_str = arr2[i]

    if min == sys.maxint:
        return
    else:
        return my_str