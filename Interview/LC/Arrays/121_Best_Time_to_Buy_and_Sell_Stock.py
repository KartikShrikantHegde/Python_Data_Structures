class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 0:
            return 0

        profit = 0
        prev_smallest = prices[0]

        for i in range(0,len(prices)):
            if prices[i] < prev_smallest:
                prev_smallest = prices[i]
                continue
            else:
                if (prices[i]-prev_smallest) > profit:
                    profit = prices[i]-prev_smallest

        return profit

my_soln = Solution()
print my_soln.maxProfit(prices=[7, 6, 4, 3, 1])