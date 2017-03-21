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

my_path = []
my_path2 = []
def find_path(root,Node):
    if root is None:
        return False

    if root.val == Node.val or find_path(root.left,Node) or find_path(root.right,Node):
        my_path.append(root.val)

    if root.val == Node.val or find_path(root.left, Node) or find_path(root.right, Node):
        my_path.append(root.val)

    return my_path[::-1]

find_path(a,h)
# print my_path
