from Linked_Lists.Single_ll.Node import Node
from Linked_Lists.Single_ll.LinkedList import LinkedList

a = Node(2)
b = Node(6)
c = Node(9)
d = Node(11)
e = Node(16)


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
        if not head:
            return None
        odd = head
        even = head.nextnode
        while even and even.nextnode is not None:
            temp = even.nextnode
            even.nextnode = even.nextnode.nextnode
            temp.nextnode = odd.nextnode
            odd.nextnode = temp
            odd = odd.nextnode
            even = even.nextnode
        return head

soln = Solution()
print soln.oddEvenList(first_list.head)
print first_list.traverseList()