class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        count = 0
        for i in range(len(haystack)):
            pos = 0
            for j in range(len(needle)):
                if haystack[i] == needle[j]:
                    pos = i
                    i += 1
                    j += 1
                    count += 1
                else:
                    if len(needle) == count:
                        return True
                    else:
                        j += 1
        return False


my_str = Solution()
print my_str.strStr(haystack="mnKartik",needle="Kartik")