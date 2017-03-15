def maj_ele(nums):
    from collections import Counter

    for k,v in Counter(nums).items():
        if v > (len(nums) / 2):
            return k

print maj_ele(nums = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2])