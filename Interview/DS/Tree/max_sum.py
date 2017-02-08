import sys

class NewNode(object):
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


a = NewNode(1)
b = NewNode(2)
c = NewNode(3)
d = NewNode(4)
e = NewNode(5)
f = NewNode(6)
g = NewNode(7)
# h = NewNode(8)

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
f.left = g
# f.right = h

def max_sum(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.val

    max_sum_left = 0
    max_sum_right = 0
    if root.left or root.right:
        max_sum_left = root.val + max_sum(root.left)
        max_sum_right = root.val + max_sum(root.right)

    if max_sum_left > max_sum_right:
        return max_sum_left
    else:
        return max_sum_right


print max_sum(a)