class NewNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = NewNode(5)
b = NewNode(3)
c = NewNode(8)
d = NewNode(9)
e = NewNode(10)


a.left = b
a.right = c
c.right = d
c.right = e

def height(root):
    if root is None:
        return False

    if root.left is None and root.right is None:
        return True


    my_val = helper()

def helper():
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    left_height = 1 + height(root.left)
    right_height = 1 + height(root.right)

    if abs(left_height - right_height) > 1:
        return False

print height(a)