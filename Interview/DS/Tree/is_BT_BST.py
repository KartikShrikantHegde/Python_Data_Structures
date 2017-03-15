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

def is_bst(root):
    return check_is_bst(root, -sys.maxint-1,sys.maxint)

def check_is_bst(root,min_val,max_val):
    if root is None:
        return True

    if root.val < min_val or root.val > max_val:
        return False

    return check_is_bst(root.left,min_val,root.val-1) and check_is_bst(root.right,root.val+1,max_val)


print is_bst(a)

# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool"""
#
#         return self.check_is_bst(root, -sys.maxint - 1, sys.maxint)
#
#     def check_is_bst(self, root, min_val, max_val):
#         if root is None:
#             return True
#
#         if root.val < min_val or root.val > max_val:
#             return False
#
#         return self.check_is_bst(root.left, min_val, root.val-1) and self.check_is_bst(root.right,
#                                                                                           root.val+1, max_val)

# my_obj = Solution()
# print my_obj.isValidBST(a)