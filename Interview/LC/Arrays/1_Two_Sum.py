class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) <=1:
            return False

        my_hash = {}
        for i in range(len(nums)):
            if nums[i] in my_hash:
                return [my_hash[nums[i]],i]
            else:
                my_hash[target - nums[i]] = i


my_sum = Solution()
print my_sum.twoSum(nums=[2,9,11,7],target=9)

