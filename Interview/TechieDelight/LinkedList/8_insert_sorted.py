from Linked_Lists.Single_ll.Node import Node
from Linked_Lists.Single_ll.LinkedList import LinkedList

a = Node(8)
b = Node(7)
c = Node(6)
d = Node(5)
e = Node(2)

e.nextnode = d
d.nextnode = c
c.nextnode = b
b.nextnode = a

my_list = LinkedList()
my_list.head = e

my_list.traverseList()

print "-----------------------------------------"
print "-----------------------------------------"

def my_insert(self,my_node):
    current = self.head
    my_temp_head = self.head

    if my_node.data < current.data:
        my_node.nextnode = current
        self.head = my_node

    while current is not None:
        prev = current
        if my_node.data < current.nextnode.data:
            my_node.nextnode = current.nextnode
            prev.nextnode = my_node
            break
        else:
            current = current.nextnode

    self.head = my_temp_head
    print self.traverseList()


f = Node(4)
my_insert(my_list,f)