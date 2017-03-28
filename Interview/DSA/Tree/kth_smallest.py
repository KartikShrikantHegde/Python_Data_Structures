from Balanced_Trees.Binary_Search_Trees.Node import Node

root = Node(10)
root.leftChild = Node(8)
root.rightChild = Node(11)
root.leftChild.leftChild = Node(7)
root.leftChild.rightChild = Node(9)
root.rightChild.rightChild = Node(12)

my_list = []


def in_order(root):
    helper(root, my_list)
    return my_list


def helper(root, my_list):
    if root is None:
        return
    if root:
        in_order(root.leftChild)
        my_list.append(root.data)
        in_order(root.rightChild)


original_val = root.data
k = 2
print in_order(root)[len(my_list) - k]
