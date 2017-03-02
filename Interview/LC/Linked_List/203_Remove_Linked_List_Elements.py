# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from Linked_Lists.single_ll.Node import Node
from Linked_Lists.single_ll.LinkedList import LinkedList

a = Node(1)
b = Node(1)
# c = Node(6)
# d = Node(3)
# e = Node(4)
# f = Node(5)
# g = Node(6)


a.nextnode = b
# b.nextnode = c
# c.nextnode = d
# d.nextnode = e
# e.nextnode = f
# f.nextnode = g


first_list = LinkedList()
first_list.head = a

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        current = head.nextnode
        prev =head

        while current:
            if prev.data == val:
                head = current
                prev = current
                current = current.nextnode
                # prev.nextnode = current
            elif current.data == val:
                current = current.nextnode
                prev.nextnode = current
            else:
                prev = current
                current = current.nextnode

        return head


my_obj = Solution()
my_obj.removeElements(a,1)
print first_list.traverseList()