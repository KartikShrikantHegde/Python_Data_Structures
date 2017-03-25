class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_local = nums[0]
        max_local = nums[0]
        max_total = nums[0]

        for i in range(1, len(nums)):
            min_local, max_local = min(nums[i], nums[i] * min_local, nums[i] * max_local), max(nums[i],
                                                                                               nums[i] * min_local,
                                                                                               nums[i] * max_local)
            max_total = max(max_local, max_total)

        return max_total

obj = Solution()
print obj.maxProduct(nums=[-2,-3,0,4])