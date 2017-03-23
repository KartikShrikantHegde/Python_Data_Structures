class NewNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.Next = None


root = NewNode(10)
root.left = NewNode(8)
root.right = NewNode(12)
root.left.left = NewNode(3)


class Binary_Tree(object):
    temp = NewNode(data=None)

    def ll_inorder(self, my_root):
        if my_root:
            self.ll_inorder(my_root.right)
            my_root.Next = Binary_Tree.temp.Next
            Binary_Tree.temp.Next = my_root
            self.ll_inorder(my_root.left)


bt = Binary_Tree()
bt.ll_inorder(root)
