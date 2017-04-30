import sys


class NewNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = NewNode(5)
b = NewNode(4)
c = NewNode(6)
# d = NewNode(4)
e = NewNode(7)
f = NewNode(5)

a.left = b
a.right = c
c.left = f
c.right = e


def is_bst(root):
    if root is None:
        return TypeError("Error")

    return check_is_bst(root, -sys.maxint - 1, sys.maxint)


def check_is_bst(root, min_val, max_val):
    if root is None:
        return True

    if root.val < min_val or root.val > max_val:
        return False

    return check_is_bst(root.left, min_val, root.val) and check_is_bst(root.right, root.val, max_val)


print is_bst(a)
