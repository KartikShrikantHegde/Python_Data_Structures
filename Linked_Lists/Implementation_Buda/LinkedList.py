__author__ = "Karthik"
import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insertStart(self, data):

        newnode = Node.Node(data)

        if not self.head:
            self.head = newnode
        else:
            newnode.nextnode = self.head
            self.head = newnode

    def size(self):

        current_node = self.head
        size = 0

        while current_node is not None:
            size += 1
            current_node = current_node.nextnode

        return size

    def traverseList(self):

        current_node = self.head

        while current_node is not None:
            print("%s " % current_node.data)
            current_node = current_node.nextnode

    def insertEnd(self, data):

        new_node = Node.Node(data)
        current_node = self.head

        while current_node.nextnode is not None:
            current_node = current_node.nextnode

        current_node.nextnode = new_node

    def remove(self, data):
        if self.head:
            if data == self.head.data:
                self.head = self.head.nextnode
            else:
                self.head.remove(data, self.head)

    def find(self, data):
        current_node = self.head

        while current_node is not None:
            if data == current_node.data:
                return "Found"
            else:
                current_node = current_node.nextnode
        return "Not Found"
