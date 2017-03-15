def max_subarray(nums):
    if not nums:
        return 0

    current_sum = max_sum = nums[0]
    for i in range(1,len(nums)):
        current_sum = max(current_sum+nums[i],nums[i])
        max_sum = max(max_sum,current_sum)

    return max_sum

print max_subarray(nums=[-2,1,3,4,-1,2,1,-5,4])