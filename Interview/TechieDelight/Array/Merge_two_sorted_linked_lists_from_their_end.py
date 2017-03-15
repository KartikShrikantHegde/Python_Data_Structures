def merge(list1,list2):
    if not list2:
        return list1
    if not list1:
        return list2
    if list1[-1] > list2[-1]:
        return [list1[-1]] + merge(list1[:-1],list2)
    return [list2[len(list2)-1]] + merge(list1,list2[:-1])

print merge(list1=[2,6,7,10],list2=[1,3,5])