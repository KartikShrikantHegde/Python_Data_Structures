class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # visited_arr = [False]*(2**20)
        # new_list = []
        # for i in range(0,len(nums)):
        #     if visited_arr[nums[i]]:
        #         new_list.append(nums[i])
        #
        #     visited_arr[nums[i]] = True
        #
        # return new_list


        from collections import Counter
        return [k for k,v in Counter(nums).items() if v > 1]

my_obj=Solution()
print my_obj.findDuplicates(nums=[4,3,2,7,8,2,3,1,7])