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


a.left = b
a.right = c
b.left = d
c.right = e


def odd_sum(root):
    odd_level = True

    return helper(root,odd_level)

def helper(root,odd_level):
    if root is None:
        return 0

    my_sum = helper(root.left,not odd_level) + helper(root.right,not odd_level)

    if odd_level:
        return root.val + my_sum
    else:
        return my_sum

print odd_sum(a)