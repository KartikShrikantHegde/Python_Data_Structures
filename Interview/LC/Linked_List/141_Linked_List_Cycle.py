from Linked_Lists.single_ll.Node import Node
from Linked_Lists.single_ll.LinkedList import LinkedList

a = Node(7)
b = Node(5)
c = Node(7)
d = Node(4)
e = Node(1)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = a

my_list = LinkedList()
my_list.head = a

# my_list.traverseList()


print "-----"

def cycle_detect(my_list):
    try:
        first = my_list.head
        second = my_list.head.nextnode

        while first is not second:
            first = first.nextnode
            second = second.nextnode.nextnode
        print first.data
        return True
    except:
        return False


print cycle_detect(my_list)
