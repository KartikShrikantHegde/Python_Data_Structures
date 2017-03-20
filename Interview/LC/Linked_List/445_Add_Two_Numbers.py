from Linked_Lists.Single_ll.Node import Node
from Linked_Lists.Single_ll.LinkedList import LinkedList

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
        str1 = ""
        str2 = ""

        while l1:
            str1 += str(l1.data)
            l1 = l1.nextnode

        while l2:
            str2 += str(l2.data)
            l2 = l2.nextnode

        str1 = int(str1)
        str2 = int(str2)

        add_sum = str1 + str2
        add_sum = str(add_sum)

        new_head = Node(add_sum[0])
        current = new_head

        for ch in add_sum[1:len(add_sum)]:
            current.nextnode = Node(ch)
            current = current.nextnode

        new_list = LinkedList()
        new_list.head = new_head

        print new_list.traverseList()

my_add = Solution()
my_add.addTwoNumbers(first_list.head,second_list.head)