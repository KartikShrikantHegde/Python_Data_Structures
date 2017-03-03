class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """

        if duration == 0:
            return 0
        if len(timeSeries) == 1:
            return max(timeSeries[0],duration)

        for i in range(len(timeSeries)):
            if timeSeries[i] + timeSeries[i+1] > duration:
                return timeSeries[i] + duration
            else:
                return max(timeSeries)

my_obj = Solution()
print my_obj.findPoisonedDuration(timeSeries=[1,2,3,4,5], duration=5)