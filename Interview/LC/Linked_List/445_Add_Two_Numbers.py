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

def merge(l1,l2):
    while l1.nextnode is not None:
        l1 = l1.nextnode

    while l2.nextnode is not None:
        l1 = l2.nextnode


merge(first_list.head,second_list.head)
print first_list.traverseList()