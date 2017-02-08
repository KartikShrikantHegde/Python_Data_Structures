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
h = NewNode(8)

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
f.left = g
f.right = h

def print_path(root,Node):
    my_list = []
    if root is None:
        return None

    if root.left is None and root.right is None:
        my_list.append(root.val)

    if root.left or root.right:
        my_list.append(root.left)

print print_path(a)