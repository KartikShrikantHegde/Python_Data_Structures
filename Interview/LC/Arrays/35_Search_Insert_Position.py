class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) / 2

            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid

        if high < 0:
            return 0

        if low > high :
            return low

my_obj = Solution()
print my_obj.searchInsert(nums=[1], target=0)
