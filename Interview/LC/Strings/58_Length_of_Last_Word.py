class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        count = 0

        for ch in s:
            if ch.isalnum():
                count += 1
            else:
                if count == 0:
                    continue
                else:
                    break

        return count

my_word = Solution()
print my_word.lengthOfLastWord(s="Hello World  ")