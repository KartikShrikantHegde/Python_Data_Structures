class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # p = 1
        # n = len(nums)
        # output = []
        # for i in range(0, n):
        #     output.append(p)
        #     p = p * nums[i]
        # p = 1
        # for i in range(n - 1, -1, -1):
        #     output[i] = output[i] * p
        #     p = p * nums[i]
        # return output

        output = []

        for i in range(len(nums)):
            left = 0
            right = len(nums) - 1
            left_product = 1
            right_product = 1
            while left < i:
                left_product = left_product * nums[left]
                left += 1

            while right > i:
                right_product = right_product * nums[right]
                right -= 1

            final_product = left_product * right_product

            output.append(final_product)

        return output

obj = Solution()
print obj.productExceptSelf(nums=[1,2,3,4])