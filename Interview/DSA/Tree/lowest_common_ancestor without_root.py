class NewNode(object):
    def __init__(self,value):
        self.val = value
        self.parent = None
        self.left = None
        self.right = None


a = NewNode(5)
b = NewNode(6)
c = NewNode(7)
d = NewNode(8)
e = NewNode(9)

a.left = b
b.parent = a
b.left = c
c.parent = b
b.right = d
d.parent = b
d.right = e
e.parent = d

def lca_without_root(c,e):
    my_list = []
    while c is not None:
        my_list.append(c)
        c = c.parent

    while e is not None:
        if e in my_list:
            return e.val
        else:
            e = e.parent

print lca_without_root(c,e)

