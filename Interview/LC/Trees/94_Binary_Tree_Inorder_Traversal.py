import sys


class NewNode(object):
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


a = NewNode(1)
b = NewNode(2)
c = NewNode(3)
# d = NewNode(10)


a.right = b
# a.right = c
b.left = c



class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        my_list = []

        self.helper(root,my_list)
        return my_list

    def helper(self,root,new_list):
        if root is None:
            return []

        if root:
            self.helper(root.left,new_list)
            new_list.append(root.val)
            self.helper(root.right,new_list)


obj = Solution()
print obj.inorderTraversal(a)