from Linked_Lists.single_ll.Node import Node
from Linked_Lists.single_ll.LinkedList import LinkedList

a = Node(7)
b = Node(2)
c = Node(4)
d = Node(3)


a.nextnode = b
b.nextnode = c
c.nextnode = d


m = Node(5)
n = Node(6)
o = Node(4)


m.nextnode = n
n.nextnode = o
# o.nextnode = p

first_list = LinkedList()
first_list.head = a

second_list = LinkedList()
second_list.head = m


print "*** Ans ***\n"

# l1 and l2 are head

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = Node(0)
        current, carry = dummy, 0

        while l1 or l2:
            data = carry
            if l1:
                data += l1.data
                l1 = l1.nextnode
            if l2:
                data += l2.data
                l2 = l2.nextnode
            carry, data = data / 10, data % 10
            current.nextnode = Node(data)
            current = current.nextnode

        if carry == 1:
            current.nextnode = Node(1)

        return dummy.nextnode


my_add = Solution()
my_add.addTwoNumbers(first_list.head,second_list.head)