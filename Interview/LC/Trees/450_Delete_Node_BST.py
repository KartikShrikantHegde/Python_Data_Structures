# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        if root.val == key:
            if root.left and root.right:
                right = root.right
                while right and right.left:
                    right = right.left
                right.left = root.left
                return root.right
            else:
                if root.left:
                    return root.left
                elif root.right:
                    return root.right
                else:
                    return None

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root