from Linked_Lists.Single_ll.Node import Node
from Linked_Lists.Single_ll.LinkedList import LinkedList

a = Node(1)
b = Node(2)
c = Node(0)
d = Node(1)
e = Node(0)

e.nextnode = d
d.nextnode = c
c.nextnode = b
b.nextnode = a

my_list = LinkedList()
my_list.head = e
my_list.traverseList()
print "\n-------------------------"

def sort_list(my_node):
    current_node = my_node

    count = [0,0,0]
    while current_node:
        count[current_node.data] += 1
        current_node = current_node.nextnode

    i = 0
    current_node = my_node

    while current_node:
        if count[i] == 0:
            i += 1
        else:
            current_node.data = i
            count[i] -= 1
            current_node = current_node.nextnode
    return

sort_list(e)
my_list.traverseList()