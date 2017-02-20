pascal triagle

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row

    --------------------------------

    class Solution:
        # @return a string
        def longestCommonPrefix(self, strs):
            if not strs:
                return ""

            for i, letter_group in enumerate(zip(*strs)):
                if len(set(letter_group)) > 1:
                    return strs[0][:i]
            else:
                return min(strs)