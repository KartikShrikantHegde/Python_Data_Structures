class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        new_str = ''
        for i in digits:
            i = str(i)
            new_str = new_str + i
        x = int(new_str) + 1
        x = str(x)
        new_list = []
        for i in x:
            i = int(i)
            new_list.append(i)
        return new_list


my_obj = Solution()
print my_obj.plusOne(digits=[9,9])