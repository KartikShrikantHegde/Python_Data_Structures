def reverse_k_list(self,head,k):

        current_node = head
        previous_node = None
        next_node = None
        count = 0

        while current_node is not None and count < k:
            next_node = current_node.nextnode
            current_node.nextnode = previous_node
            previous_node = current_node
            current_node = next_node
            count += 1

        if next_node is not None:
            head.nextnode = self.reverse_k_list(next_node,k)

        return previous_node