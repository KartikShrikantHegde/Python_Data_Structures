class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        '''sets the values to null but returns correct len'''
        # counter = 0
        # for x in range(len(nums)):
        #     if nums[x] == val:
        #         nums.remove(val)
        #         nums.insert(0,None)
        #         counter += 1
        # print nums,counter
        # return len(nums) - counter



    # This is a two pointer soln and makes sure array values are preserved

        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start


my_ele = Solution()
print my_ele.removeElement(nums = [3,2,2,3], val = 3)