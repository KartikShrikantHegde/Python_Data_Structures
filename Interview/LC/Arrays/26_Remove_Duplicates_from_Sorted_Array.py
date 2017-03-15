class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        # if not A:
        #     return 0
        #
        # newTail = 0
        #
        # for i in range(1, len(A)):
        #     if A[i] != A[newTail]:
        #         newTail += 1
        #         A[newTail] = A[i]
        #
        # return newTail + 1
        from collections import Counter
        temp = 0
        for k, v in Counter(A).items():
            if v > 1:
                temp +=1

        return temp


my_obj = Solution()
print my_obj.removeDuplicates(A=[1,1,1,1,1,2,2,2,3,3])

