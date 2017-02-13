def duplicate(nums):
    return len(nums) != len(set(nums))

print duplicate(nums=[10,20,30,40,20])