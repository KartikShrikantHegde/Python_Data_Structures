class NewNode(object):
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


a = NewNode(10)
b = NewNode(16)
c = NewNode(5)
d = NewNode(-3)
e = NewNode(6)
f = NewNode(11)


a.left = b
a.right = c
b.right = d
c.left = e
c.right = f

def sum_possible(root,k):

    return my_sum_possible(root,k)

my_list = []
def my_sum_possible(root,k):

    if root is None:
        return False

    # if k == root.val:
    #     return True

    if k == root.val or my_sum_possible(root.left,k - root.val) or my_sum_possible(root.right, k - root.val):
        my_list.append(root.val)
        return True, my_list

    return False

print sum_possible(a,25)