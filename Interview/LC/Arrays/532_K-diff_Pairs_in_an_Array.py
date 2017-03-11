class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """


        nums = list(set(nums))
        my_dict = {}
        count = 0
        my_dict[nums[0]] = abs(k - nums[0])
        for i in range(1,len(nums)):
            my_dict[nums[i]] = abs(k-nums[i])
            if my_dict[nums[i]] in my_dict.keys():
                count += 1

        return count

my_obj = Solution()
print my_obj.findPairs(nums=[1, 3, 1, 5, 4],k=0)