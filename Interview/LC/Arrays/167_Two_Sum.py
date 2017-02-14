class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # for i in range(0,len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1,j+1]

        l , r = 0, len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return l+1,r+1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1



my_soln = Solution()
print my_soln.twoSum(numbers=[2,7,11,15],target=9)