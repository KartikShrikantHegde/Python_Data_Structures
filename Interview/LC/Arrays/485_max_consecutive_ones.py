class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max_ones = 0
        local_max_ones = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                local_max_ones = local_max_ones + 1
                if local_max_ones > global_max_ones:
                    global_max_ones = local_max_ones
            else:
                local_max_ones = 0


        return global_max_ones

my_arr = [1,1,0,1,1,1,0,0,0,1,1,1,1,1]
new = Solution()
new.findMaxConsecutiveOnes(my_arr)