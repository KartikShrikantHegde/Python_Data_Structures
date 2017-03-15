import sys

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

        if self.left:
            self.left.inorder()

        print self.data

        if self.right:
            self.right.inorder()


my_tree = NewNode(7)
# my_tree.insert(7)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(9)
my_tree.insert(8)

my_tree.inorder()
