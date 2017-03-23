from Node import Node


class BinarySearchTree(object):
    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        if not self.rootNode:
            self.rootNode = Node(data)
        else:
            self.rootNode.insert(data)

    def remove(self, dataToRemove):
        if self.rootNode is Node:
            return None

        if self.rootNode.data == dataToRemove:
            if self.rootNode.right and self.rootNode.left:
                self.right = self.rootNode.right
                while self.right is not None and self.right.left:
                    self.right = self.right.left
                self.right.left = self.rootNode.left
            else:
                if self.rootNode.left:
                    self.rootNode = self.rootNode.left
                elif self.rootNode.right:
                    self.rootNode = self.rootNode.right
                else:
                    self.rootNode = None

        elif dataToRemove > self.rootNode.data:
            self.rootNode.right = self.remove(dataToRemove)
        else:
            self.rootNode.left = self.remove(dataToRemove)


                    # if self.rootNode:
        #     if self.rootNode.data == dataToRemove:
        #         tempNode = Node(None)
        #         tempNode.leftChild = self.rootNode
        #         self.rootNode.remove(dataToRemove, tempNode)
        #         self.rootNode = tempNode.leftChild
        #     else:
        #         self.rootNode.remove(dataToRemove, None)

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
        if self.rootNode:
            self.rootNode.traverseInOrder()
        # current_node = self.rootNode
        # if current_node:
        #     if current_node.leftChild:
        #         current_node.leftChild.traverseInOrder()
        #
        #     print(current_node.data)
        #
        #     if current_node.rightChild:
        #         current_node.rightChild.traverseInOrder()