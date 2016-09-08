class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        my_n = bin(n)
        for ch in my_n:
            if ch == '1':
                count += 1

        return count