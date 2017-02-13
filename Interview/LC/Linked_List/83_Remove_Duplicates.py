from Linked_Lists.single_ll.Node import Node
from Linked_Lists.single_ll.LinkedList import LinkedList

a = Node(1)
b = Node(2)
c = Node(2)
# d = Node(3)
# e = Node(3)


a.nextnode = b
b.nextnode = c
# c.nextnode = d
# d.nextnode = e

my_list = LinkedList()
my_list.head = a

my_list.traverseList()


print "-----"

def duplicate(my_list):
    current = my_list.head
    while current:
        while current.nextnode and current.nextnode.data == current.data:
            current.nextnode = current.nextnode.nextnode
        current = current.nextnode

    my_list.traverseList()


duplicate(my_list)

