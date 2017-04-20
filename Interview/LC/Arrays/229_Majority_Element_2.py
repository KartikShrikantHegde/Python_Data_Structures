from collections import Counter

def t(nums):
    res = []
    ctr = Counter(nums).iteritems()
    for key,value in ctr:
        if value > (len(nums) // 3):
            res.append( key)

    return res

print t(nums=[1,2,3,1,1,1,2,2,2])