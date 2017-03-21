from Node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self,val):
        new_node = Node(val)
        current_node = self.head
        if current_node is not None:
            new_node.nextnode = current_node
            while current_node.nextnode != self.head:
                current_node = current_node.nextnode
            current_node.nextnode = new_node
        else:
            new_node.nextnode = new_node  # For the first node

        self.head = new_node

    def traverse(self):
        current_node = self.head

        while current_node.nextnode != self.head:
            print current_node.val
            current_node = current_node.nextnode
            if current_node.nextnode == self.head:
                print current_node.val
