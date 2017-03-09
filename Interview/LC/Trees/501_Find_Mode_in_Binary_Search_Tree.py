import sys


class NewNode(object):
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


a = NewNode(1)
c = NewNode(2)
d = NewNode(2)

a.right = c
c.left = d

import collections
count = collections.defaultdict(int)

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root:
            # print count[root.val]
            count[root.val] += 1
            # print count
            self.findMode(root.left)
            self.findMode(root.right)

my_mode = Solution()
my_mode.findMode(a)
print count
print max(count.itervalues())
# print [k for k, v in count.iteritems() if v == max_ct]