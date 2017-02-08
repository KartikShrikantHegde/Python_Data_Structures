from Balanced_Trees.Binary_Search_Trees.Node import Node

root = Node(10)
root.leftChild = Node(-10)
root.rightChild = Node(30)
root.leftChild.rightChild = Node(8)
root.leftChild.rightChild.leftChild = Node(6)
root.leftChild.rightChild.rightChild = Node(9)


def findlca(root, n1, n2):
    if root.data > (max(n1, n2)):
        return findlca(root.leftChild, n1, n2)
    elif root.data < min(n1, n2):
        return findlca(root.rightChild, n1, n2)
    else:
        return root.data


print findlca(root, 8, -10)
