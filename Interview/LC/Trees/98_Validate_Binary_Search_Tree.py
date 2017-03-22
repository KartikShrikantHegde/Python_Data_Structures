import sys


class NewNode(object):
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


a = NewNode(1)
b = NewNode(1)
# c = NewNode(15)
# d = NewNode(10)

a.left = b
# a.right = c
# b.right = d


class Solution(object):
    def isValidBST(self, root, min_val=-sys.maxint - 1, max_val=sys.maxint):
        """
        :param max_val:
        :param min_val:
        :type root: TreeNode
        :rtype: bool"""

        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.isValidBST(root.left, min_val, root.val) and self.isValidBST(root.right, root.val, max_val)


obj = Solution()
print obj.isValidBST(a)