__author__ = "Karthik Hegde"

import Node

class LinkedList(object):
    def __init__(self,head = None):
        self.head = head                             # Set Head to none intially
        self.size = 0

    def getsize(self):
        return self.size

    def add(self,data):
        newnode =   Node.Node(data,self.head)
        self.head = newnode
        self.size += 1

    def remove(self,d):
        current_node = self.head
        prev_node = None

        while current_node:
            if current_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(current_node.get_next())
                else:
                    self.head = current_node
                self.size -=1
                return True
            else:
                prev_node = current_node
                current_node = current_node.get_next()
        return False

    def find(self,d):
        current_node = self.head

        while current_node:
            if current_node.get_data() == d:
                return d
            else:
                current_node = current_node.get_next()
        return None







