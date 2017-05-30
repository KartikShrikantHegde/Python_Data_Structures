class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}

        for i in xrange(len(list1)):
            d[list1[i]] = i

        final_dict = {}
        for j in xrange(len(list2)):
            if list2[j] in d.keys():
                final_dict[list2[j]] = j + d[list2[j]]

        min_val = min(final_dict.itervalues())

        return [key for key, value in final_dict.iteritems() if value == min_val]