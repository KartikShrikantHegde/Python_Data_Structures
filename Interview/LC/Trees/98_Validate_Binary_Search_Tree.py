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
    def isValidBST(self, root, lessThan=-sys.maxint - 1, largerThan=sys.maxint):
        """
        :type root: TreeNode
        :rtype: bool"""

        if not root:
            return True
        if root.val <= lessThan or root.val >= largerThan:
            return False
        return self.isValidBST(root.left, lessThan, root.val) and self.isValidBST(root.right, root.val, largerThan)