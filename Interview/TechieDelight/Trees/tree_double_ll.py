from Linked_Lists.Doubly_LL.LinkedList import LinkedList

class NewNode(object):
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = NewNode(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = NewNode(data)
                else:
                    self.right.insert(data)

    def inorder(self):

        if self.right:
            self.right.inorder()

        new_list.add(self.data)
        # print new_list.head.val

        if self.left:
            self.left.inorder()


my_tree = NewNode(7)
# my_tree.insert(7)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(9)
my_tree.insert(8)


new_list = LinkedList()
my_tree.inorder()
print new_list.traverse_list()