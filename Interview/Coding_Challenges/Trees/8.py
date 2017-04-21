class NewNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = NewNode(5)
b = NewNode(3)
c = NewNode(8)
d = NewNode(6)
e = NewNode(4)
f = NewNode(2)
m = NewNode(1)
g = NewNode(12)
h = NewNode(10)
i = NewNode(15)
j = NewNode(9)

a.left = b
a.right = c
b.left = f
b.right = e
f.left = m
c.left = d
c.right = g
g.left = h
g.right = i
h.left = j


def get_next(root, node):
    if root is None:
        return TypeError("Error")

    if root.val > node.val:
        left_side = _get_next(root, node)
        return left_side.val
    else:
        right_side = _get_nextt(root, node)
        return right_side.val


def _get_next(prev, current):
    temp = prev
    while prev.val > current.val:
        temp = prev
        prev = prev.left

    return temp


def _get_nextt(prev, current):
    temp = prev
    while prev.val <= current.val:
        temp = prev
        prev = prev.right

    return temp


print get_next(a, f)
