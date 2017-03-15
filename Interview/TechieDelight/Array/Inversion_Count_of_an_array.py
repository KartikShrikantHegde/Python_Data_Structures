def inversion(nums):
    count = 0

    for i in range(len(nums)):
        j = len(nums) - 1
        while i < j:
            if nums[i] > nums[j]:
                count += 1
                j -= 1
            else:
                j -= 1

    return count


print inversion(nums=[1, 9, 6, 1, 5])