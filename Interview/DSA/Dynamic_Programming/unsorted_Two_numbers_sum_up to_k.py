class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # if len(nums) <=1:
        #     return False

        my_hash = {}
        for i in range(len(nums)):
            if nums[i] in my_hash:
                return [nums[my_hash[nums[i]]],nums[i]]
            else:
                my_hash[target - nums[i]] = i

        return False

my_sum = Solution()
print my_sum.twoSum(nums=[2],target=11)

