class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a = set('qwertyuiop')
        b = set('asdfghjkl')
        c = set('zxcvbnm')
        result = []
        for word in words:
            t =  set(word.lower())
            if a & t == t:
                result.append((word))
            if b & t == t:
                result.append((word))
            if c & t == t:
                result.append((word))

        return result


my_hash = Solution()
print my_hash.findWords(words=["Hello", "Alaska", "Dad", "Peace"])