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
f = NewNode(8)
g = NewNode(6)
h = NewNode(9)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
f.left = g
f.right = h

def odd_sum(root):
    if root is None:
        return 0
    return root.val - odd_sum(root.left) - odd_sum(root.right)

print odd_sum(a)