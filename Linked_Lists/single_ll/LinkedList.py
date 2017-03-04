__author__ = "Karthik"

import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insertStart(self, data):

        newnode = Node.Node(data)
        current = self.head
        if not current:
            self.head = newnode
        else:
            self.head = newnode
            self.head.nextnode = current

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
                current = self.head.nextnode
                prev = self.head
                while current:
                    if current.data == data:
                        current = current.nextnode
                        prev.nextnode = current
                        break
                    else:
                        prev = current
                        current = current.nextnode
        else:
            print "List is Empty. Cannot remove elements from empty list"

    def find(self, data):
        current_node = self.head

        while current_node is not None:
            if data == current_node.data:
                return "Found"
            else:
                current_node = current_node.nextnode
        return "Not Found"

    def reverse_list(self):

        current_node = self.head
        previous_node = None

        while current_node:
            temp_node = current_node.nextnode
            current_node.nextnode = previous_node
            previous_node = current_node
            current_node = temp_node

        self.head = previous_node

    def rec_reverse(self):

        if self.head is None:
            return None

        self.rec_reverse_util(self.head, None)

    def rec_reverse_util(self, current, prev):
        if current.nextnode is None:
            self.head = current
            current.nextnode = prev
            return

        next = current.nextnode
        current.nextnode = prev

        self.rec_reverse_util(next, current)

    # def fold(self):
    #     slow = self.head
    #     fast = self.head
    #
    #     while fast is not None:
    #         slow = slow.nextnode
    #         fast = fast.nextnode
    #
    #         if fast is not None:
    #             fast = fast.nextnode
    #
    #     middle = slow
    #     self.head = slow
    #     reverse = self.rec_reverse
    #
    #     while reverse is not None and self.head != middle:
    #         tempHead = head.nextnode
    #         tempReverse = reverse.nextnode
    #         reverse.nextnode = head.nextnode
    #         self.head.nextnode = reverse
    #         head = tempHead
    #         reverse = tempReverse
    #     if reverse is not None:
    #         reverse.nextnode = None
    #     else:
    #         self.head.nextnode = None


    def reverse_k_list(self, head, k):

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
            head.nextnode = self.reverse_k_list(next_node, k)

        return previous_node
