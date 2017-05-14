def summaryRanges(nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if not nums:
            return []

        if len(nums) == 1:
            return [str(nums[0])]

        ranges = []
        start = nums[0]
        end = nums[0]

        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                end = nums[i]
                continue
            else:
                ranges.append(get_range(start, end))
                start = nums[i]
                end = nums[i]

        if start <= end:
            ranges.append(get_range(start, end))

        return ranges

def get_range(n1, n2):
    if n1 == n2:
        return str(n1)
    else:
        return str(n1) + "->" + str(n2)

print summaryRanges(nums=[0,1])