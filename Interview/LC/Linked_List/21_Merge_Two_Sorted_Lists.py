from Linked_Lists.Single_ll.Node import Node
from Linked_Lists.Single_ll.LinkedList import LinkedList

a = Node(1)
b = Node(3)
c = Node(5)
d = Node(7)


a.nextnode = b
b.nextnode = c
c.nextnode = d


m = Node(2)
n = Node(4)
o = Node(6)
p = Node(8)



m.nextnode = n
n.nextnode = o
o.nextnode = p

first_list = LinkedList()
first_list.head = a

second_list = LinkedList()
second_list.head = m


print "*** Ans ***\n"

# l1 and l2 are head

def merge(l1,l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.data < l2.data:
        l1.nextnode = merge(l1.nextnode, l2)
        return l1
    else:
        l2.nextnode = merge(l1, l2.nextnode)
        return l2

merge(first_list.head,second_list.head)
print first_list.traverseList()
# print second_list.traverseList()