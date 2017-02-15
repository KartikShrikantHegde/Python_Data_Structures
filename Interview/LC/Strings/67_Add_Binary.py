class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2)
        b = int(b, 2)

        my_sum = a + b

        my_sum = bin(my_sum)
        return my_sum[2:]


my_bin = Solution()
print my_bin.addBinary(a="11",b="1")