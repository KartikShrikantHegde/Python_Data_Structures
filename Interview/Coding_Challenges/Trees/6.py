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


def _check_balance(node):
    if node is None:
        return 0
    left_height = _check_balance(node.left)
    if left_height == -1:
        return -1
    right_height = _check_balance(node.right)
    if right_height == -1:
        return -1
    diff = abs(left_height - right_height)
    if diff > 1:
        return -1
    return 1 + max(left_height, right_height)


def check_balance(root):
    if root is None:
        raise TypeError('root cannot be None')
    height = _check_balance(root)
    return height != -1


print check_balance(a)
