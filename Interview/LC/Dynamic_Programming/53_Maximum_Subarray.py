class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in range(1,len(nums)):
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


my_obj = Solution()
print my_obj.maxSubArray(nums = [1])