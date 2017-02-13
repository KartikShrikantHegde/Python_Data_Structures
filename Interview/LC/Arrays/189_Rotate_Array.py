def rotate(nums, k):
    n = len(nums)
    nums[:] = nums[n - k:] + nums[:n - k]

    print nums

rotate(nums=[1,2],k=0)