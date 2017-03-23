from Balanced_Trees.Binary_Search_Trees.Node import Node

root = Node(1)
root.leftChild = Node(2)
root.rightChild = Node(3)
root.leftChild.rightChild = Node(4)
root.rightChild.rightChild = Node(6)
root.rightChild.leftChild = Node(5)



def findlca(root, n1, n2):
    if root.data > (max(n1, n2)):
        return findlca(root.leftChild, n1, n2)
    elif root.data < min(n1, n2):
        return findlca(root.rightChild, n1, n2)
    else:
        return root.data


print findlca(root, 2, 5)
