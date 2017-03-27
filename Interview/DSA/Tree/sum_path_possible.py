class NewNode(object):
    def __init__(self, value):
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

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
f.left = g


def sum_possible(root, k):

    if root is None:
        return None

    if root.val == k or sum_possible(root.left, k - root.val) or sum_possible(root.right,k-root.val):
        return True

    return False


# def my_sum_possible(root, k, original_k):
#     if root is None:
#         return False
#
#     if k == root.val:
#         return True
#
#     return my_sum_possible(root.left, k - root.val, original_k) or my_sum_possible(root.right, k - root.val,original_k) or my_sum_possible(root.left,original_k,original_k) or my_sum_possible(root.right, original_k, original_k)

print sum_possible(a, 8)