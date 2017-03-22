class NewNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = NewNode(3)
b = NewNode(6)
c = NewNode(4)
d = NewNode(9)
e = NewNode(7)


a.left = b
a.right = c
b.left = d
b.right = e


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        if root.val == p.val or root.val == q.val:
            return root.val

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left is not None and right is not None:
            return root.val

        if left is None and right is None:
            return None

        if left is None and right is not None:
            return right.val
        else:
            return left.val


obj = Solution()
print obj.lowestCommonAncestor(a, a, c)
