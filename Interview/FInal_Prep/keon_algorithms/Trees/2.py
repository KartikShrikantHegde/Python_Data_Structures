class Node():
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

def bintree2list(root):
    """
    type root: root class
    """
    if not root:
        return root

    head = None
    x = bintree2list_util(root,head)

def bintree2list_util(root,head):
    temp_head = Node()
    if root.left:
        bintree2list_util(root.left,head)

    if not head:
        head = root.val
        temp = root.val

    if temp_head.left is None:
        root.left = head.val
    if temp_head.right is None:
        head.right = root.val

    head = root

    if root.right:
        bintree2list_util(root.right,head)

def print_tree(root):
    while root:
        print(root.val)
        root = root.right

tree = Node(10)
tree.left = Node(12)
tree.right = Node(15)
tree.left.left  = Node(25)
tree.left.left.right  = Node(100)
tree.left.right = Node(30)
tree.right.left = Node(36)

head = bintree2list(tree)
print_tree(head)