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

a.left = b
b.right = c
a.right = d
d.right = f
d.left = e

def binaryTreePaths(root):
    res = []
    if not root:
        return res
    DFS(res, root, str(root.val))
    return res

def DFS(res, root, cur):
    if not root.left and not root.right:
        res.append(cur)
    if root.left:
        DFS(res, root.left, cur+'->'+str(root.left.val))
    if root.right:
        DFS(res, root.right, cur+'->'+str(root.right.val))

print binaryTreePaths(a)