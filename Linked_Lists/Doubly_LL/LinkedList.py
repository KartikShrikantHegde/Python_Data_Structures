from Node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def add(self,data):
        new_node = Node(data)
        current_node = self.head
        if current_node:
            self.head = new_node
            new_node.set_next(current_node)
            current_node.set_prev(self.head)
            self.size += 1
        else:
            self.head = new_node
            self.size += 1

    def remove(self,data):
        current_node = self.head
        while current_node:
            if self.head.get_data() == data:
                nextnode = self.head.get_next()
                self.head = nextnode
                break
            else:
                current_node = current_node.get_next()
                if current_node.get_data() == data:
                        nextnode = current_node.get_next()
                        prev = current_node.get_prev()
                        prev.set_next(nextnode)
                        if nextnode:
                            nextnode.set_prev(prev)
                        break

    def traverse_list(self):
        current_node = self.head

        while current_node:
            print current_node.get_data()
            current_node = current_node.get_next()





