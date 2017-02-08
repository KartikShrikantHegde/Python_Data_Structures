def reverse_list(self):


        current_node = self.head
        previous_node = None

        while current_node is not None:
            next_node = current_node.nextnode
            current_node.nextnode = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node