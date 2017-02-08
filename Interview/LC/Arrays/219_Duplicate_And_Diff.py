def containsNearbyDuplicate(nums, k):
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False


print containsNearbyDuplicate(nums=[1,2,3,4,2,5],k = 6)