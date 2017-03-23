class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                return [nums[i],nums[j]]


my_sum = Solution()
print my_sum.twoSum(nums=[2,7,9,11],target=9)