class NewNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = NewNode(5)
b = NewNode(3)
c = NewNode(8)
d = NewNode(1)
e = NewNode(4)

a.left = b
a.right = c
c.right = d
d.right = e


def height(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    left_height = 1 + height(root.left)
    right_height = 1 + height(root.right)

    return max(left_height, right_height)


print height(a)
