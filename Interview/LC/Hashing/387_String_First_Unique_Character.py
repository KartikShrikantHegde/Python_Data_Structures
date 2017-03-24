from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        return min([s.find(c) for c, v in Counter(s).iteritems() if v == 1] or [-1])

        # import collections
        #
        # d = collections.OrderedDict()
        # for ch in s.lower():
        #     if ch in d.iterkeys():
        #         d[ch] = d[ch] + 1
        #     else:
        #         d[ch] = 1
        #
        # for key, val in d.iteritems():
        #     if val == 1:
        #         return s.index(key)
        #     else:
        #         continue
        #
        # return -1


obj = Solution()
print obj.firstUniqChar(s='loveleetcodey')