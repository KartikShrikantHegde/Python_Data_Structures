class NewNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = NewNode(1)
b = NewNode(4)
c = NewNode(3)
# d = NewNode(2)
e = NewNode(5)

a.left = b
a.right = c


# c.left = d
c.right = e


class something():
    def findTilt(self, root):
        self.ans = 0

        def _sum(node):
            if not node: return 0
            left = _sum(node.left)
            right = _sum(node.right)
            self.ans += abs(left - right)
            return node.val + left + right

        _sum(root)
        return self.ans


obj = something()
print obj.findTilt(a)
