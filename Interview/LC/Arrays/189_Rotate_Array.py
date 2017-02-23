def rotate(nums, k):
    n = len(nums) -1
    nums[:] = nums[n - k:] + nums[:n - k]

    print nums

rotate(nums=[1,2,3,4,5],k=2)