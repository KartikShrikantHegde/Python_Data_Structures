class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 0:
            return 0

        prev_val = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] > prev_val:
                profit += (prices[i] - prev_val)
            prev_val = prices[i]

        return profit

my_profit = Solution()
print my_profit.maxProfit(prices=[1,2,4])