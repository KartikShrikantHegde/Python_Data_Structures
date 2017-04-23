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
g = NewNode(12)
m = NewNode(2)
k = NewNode(1)
v = NewNode(4)
q = NewNode(7)
s = NewNode(10)
z = NewNode(15)
l = NewNode(9)

a.left = b
a.right = c
e.left = v
b.right = e
b.left = m
c.left = d
c.right = g
m.left = k
d.right = q
g.left = s
g.right = z
s.left = l

def get_next(root, p):
    succ = None
    while root:
        if p.val < root.val:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ.val

print get_next(a, c)
