class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # my_dict = {}
        # values = 0
        # max_ele = max(nums)
        # nums.remove(max_ele)
        # nums = list(set(nums))
        # for i in range(0,len(nums)):
        #     my_dict[i] = max_ele - nums[i]
        #
        # for value in my_dict.values():
        #     values += value
        #
        # return values
        counter = 0
        while len(set(nums)) != 1:
            counter += 1
            max_ele = max(nums)
            nums.remove(max_ele)
            for i in range(0,len(nums)):
                nums[i] += 1
            nums.append(max_ele)

        return counter

my_sol = Solution()
print my_sol.minMoves(nums=[5,6,8,8,5])