class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        from collections import Counter
        if k == 0:
            for k,v in Counter(nums).items():
                if v >= 2:
                    count += 1
            return count

        count = 0
        c = Counter(nums)
        for key in c:
            if key + k in c:
                count += 1

        return count

my_obj = Solution()
print my_obj.findPairs(nums=[1,2,3,4,5],k=3)

