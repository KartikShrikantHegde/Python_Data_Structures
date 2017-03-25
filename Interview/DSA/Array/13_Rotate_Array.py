def rotate(nums, k):
    n = len(nums) -1
    nums[:] = nums[n - k:] + nums[:n - k]

    print nums

rotate(nums=[],k=2)