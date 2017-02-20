class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        i = 0
        total = 0

        while i < len(s):
            if (i + 1) < len(s):
                if roman[s[i]] >= roman[s[i+1]]:
                    total += roman[s[i]]
                    i += 1
                else:
                    total = total + roman[s[i+1]] - roman[s[i]]
                    i += 2
            else:
                total += roman[s[i]]
                i += 1

        return total



my_obj = Solution()
print my_obj.romanToInt(s="XI")