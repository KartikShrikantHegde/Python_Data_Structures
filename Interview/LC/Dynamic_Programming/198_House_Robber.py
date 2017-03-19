class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        odd = 0

        for i in range(0,len(nums)):
            if i % 2 == 0:
                even = even + nums[i]
                even = even if even > odd else odd
            else:
                odd = odd + nums[i]
                odd = even if even > odd else odd

        return max(even,odd)

obj = Solution()
print obj.rob(nums=[3,2,1,4])