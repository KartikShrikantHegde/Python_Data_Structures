class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        import collections
        # counter = collections.Counter()
        # for bricks in wall:
        #     cumsum = 0
        #     for i in xrange(len(bricks) - 1):
        #         cumsum += bricks[i]
        #         counter[cumsum] += 1
        # return len(wall) - max(counter.values())

        d = collections.defaultdict(int)
        for line in wall:
            i = 0
            for brick in line[:-1]:
                i += brick
                d[i] += 1
        # print len(wall), d
        print d.values() + [0]
        return len(wall) - max(d.values() + [0])


my_obj = Solution()
print my_obj.leastBricks(wall=[[1,1,1]])