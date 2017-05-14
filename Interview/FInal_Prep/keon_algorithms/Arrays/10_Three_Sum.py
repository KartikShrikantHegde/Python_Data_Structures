def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:  # deal with special input
        return []
    elif len(nums) == 3:
        if sum(nums) == 0:
            return [sorted(nums)]

    nums = sorted(nums)  # sorted, O(nlgn)
    ans = []

    for i in xrange(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1  # hence i < j < k

        while j < k:  # if not cross line
            temp_sum = nums[i] + nums[j] + nums[k]
            if temp_sum == 0:
                ans.append((nums[i], nums[j], nums[k]))

            if temp_sum > 0:  # which means we need smaller sum, move k backward, remember we sort the array
                k -= 1
            else:
                j += 1

    return list(set(tuple(ans)))

s = [-1, 0, 1, 2, -1, -4]
print threeSum(s)