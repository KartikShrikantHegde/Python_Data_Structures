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
        if not head:
            return head
        odd = head
        even = head.nextnode
        while even and even.nextnode != None:
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