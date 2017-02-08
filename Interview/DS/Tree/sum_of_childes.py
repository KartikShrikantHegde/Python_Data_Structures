from Balanced_Trees.Binary_Search_Trees.Node import Node

root = Node(1)
root.leftChild = Node(2)
root.rightChild = Node(3)
root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.rightChild.rightChild = Node(8)
root.rightChild.rightChild.leftChild = Node(6)
root.rightChild.rightChild.rightChild = Node(7)


def sum_of_child(root):
    if root is None:
        return 0

    if root.leftChild is not None or root.rightChild is not None:
        sum = sum_of_child(root.leftChild) + sum_of_child(root.rightChild)
        root.data += sum
    return root.data


def in_order(root):
    if root is None:
        return
    in_order(root.leftChild)
    print root.data
    in_order(root.rightChild)

original_val = root.data
print sum_of_child(root) - original_val
print in_order(root)
