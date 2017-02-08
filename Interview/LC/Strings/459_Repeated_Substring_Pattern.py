class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        print (2 * str)[1:-1]
        return str in (2 * str)[1:-1]


my_obj = Solution()

print my_obj.repeatedSubstringPattern('abab')