# Calculate the no of 1's in the binary no of a decimal

# # Steps:
#   1. AND N with 1
#   2. if the result is one increment count
#   3. bit-shift n by 1
#   4. repeat until N is 0

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0
        while n:
            if n & 1:
                res += 1
            n = n >> 1
        return res

my_sol = Solution()
print my_sol.hammingWeight(11)
