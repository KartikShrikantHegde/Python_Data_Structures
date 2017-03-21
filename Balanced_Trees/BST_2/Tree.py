from NODE import Node

class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            nd = self.root
            while nd is not None:
                if item < nd.data:
                    if nd.left is None:
                        nd.left = Node(item)
                        return
                    else:
                        nd = nd.left
                else:
                    if nd.right is None:
                        nd.right = Node(item)
                        return
                    else:
                        nd = nd.right

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print node.data
            self.inorder(node.right)