from Linked_Lists.single_ll.Node import Node
from Linked_Lists.single_ll.LinkedList import LinkedList

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)


a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

first_list = LinkedList()
first_list.head = a

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1 = odd = Node(0)
        dummy2 = even = Node(0)
        while head:
            odd.nextnode = head
            even.nextnode = head.nextnode
            odd = odd.nextnode
            even = even.nextnode
            head = head.nextnode.nextnode if even else None
        odd.nextnde = dummy2.nextnode
        return dummy1.nextnode

soln = Solution()
print soln.oddEvenList(first_list.head)
print first_list.traverseList()