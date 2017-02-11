from Linked_Lists.single_ll.Node import Node
from Linked_Lists.single_ll.LinkedList import LinkedList

a = Node(7)
b = Node(5)
c = Node(7)


a.nextnode = b
b.nextnode = c


my_list = LinkedList()
my_list.head = a

my_list.traverseList()


print "-----"

def is_palindrome(my_list):
    if my_list.head is None:
        return True

    if my_list.head.nextnode is None:
        return True

    current_node = my_list.head
    my_str = ""
    while current_node is not None:
        my_str = my_str + str(current_node.data)
        current_node = current_node.nextnode

    return (my_str == my_str[::-1])

print is_palindrome(my_list)