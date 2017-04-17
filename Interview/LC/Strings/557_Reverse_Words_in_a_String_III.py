class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #
        # if not s:
        #     return None
        #
        # if len(s)==0:
        #     return s


        my_list = s.split()
        for i in range(0, len(my_list)):
            my_list[i] = my_list[i][::-1]

        return " ".join(my_list)


my_obj = Solution()
print my_obj.reverseWords(s='')
