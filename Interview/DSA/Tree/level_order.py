from Balanced_Trees.Binary_Search_Trees.Node import Node

root = Node(10)
root.leftChild = Node(20)
root.rightChild = Node(30)
root.leftChild.leftChild = Node(40)
root.leftChild.rightChild = Node(50)
root.rightChild.leftChild = Node(60)
root.rightChild.rightChild = Node(70)



def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root == None:
        return []

    res = []
    nodes = [root]
    while nodes:
        res.append([node.data for node in nodes])
        next_nodes = []
        for node in nodes:
            if node.leftChild:
                next_nodes.append(node.leftChild)
            if node.rightChild:
                next_nodes.append(node.rightChild)
        nodes = next_nodes

    return res

print levelOrder(root)