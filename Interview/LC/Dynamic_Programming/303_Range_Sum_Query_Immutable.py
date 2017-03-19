class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = nums
        for i in xrange(1, len(nums)):
            self.dp[i] += self.dp[i - 1]
        print self.dp

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # left_sum = 0
        # right_sum = 0
        #
        # while i <= j:
        #     left_sum += self.nums[i]
        #     i += 1
        #     right_sum += self.nums[j]
        #     j -=1
        #
        # if i == j:
        #     return left_sum + right_sum + self.nums[i]
        # return left_sum + right_sum




        return self.dp[j] - (self.dp[i - 1] if i > 0 else 0)


obj = NumArray(nums=[-2,0,3,-5,2,-1])
print obj.sumRange(0,5)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
