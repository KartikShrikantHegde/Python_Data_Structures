from Node import Node


class BinarySearchTree(object):
    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        if (not self.rootNode):
            self.rootNode = Node(data)
        else:
            self.rootNode.insert(data)

    def remove(self, dataToRemove):
        if (self.rootNode):
            if self.rootNode.data == dataToRemove:
                tempNode = Node(None)
                tempNode.leftChild = self.rootNode
                self.rootNode.remove(dataToRemove, tempNode)
                self.rootNode = tempNode.leftChild
            else:
                self.rootNode.remove(dataToRemove, None)

    def getMax(self):

        maxNode = self.rootNode

        while maxNode.rightChild:
            maxNode = maxNode.rightChild

        return maxNode.data

    def getMin(self):

        minNode = self.rootNode

        while minNode.leftChild:
            minNode = minNode.leftChild

        return minNode.data

    def traverseInOrder(self):
        current_node = self.rootNode
        if current_node:
            if current_node.leftChild:
                current_node.leftChild.traverseInOrder()

            print(current_node.data)

            if current_node.rightChild:
                current_node.rightChild.traverseInOrder()