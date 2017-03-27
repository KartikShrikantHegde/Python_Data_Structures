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


def print_path(root):
    my_arr = [None]*1000
    helper(root,my_arr,0)

def helper(root,my_arr,lent):
    if root is None:
        return

    my_arr[lent] = root.val
    lent += 1

    if root.left is None and root.right is None:
        printarray(my_arr,lent)
    else:
        helper(root.left,my_arr,lent)
        helper(root.right,my_arr,lent)

def printarray(my_arr,lent):
    for i in range(0,lent):
        print my_arr[i]

print_path(a)