class BST(object):
    def __init__(root,data):
        root.left = None
        root.right = None
        root.data = data

def insert(root,node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left in None:
                root.left = node
            else:
                insert(root.left,node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)





