from Linked_Lists.single_ll.Node import Node
from Linked_Lists.single_ll.LinkedList import LinkedList

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(25)


a.nextnode = b
b.nextnode = c
c.nextnode = d
# d.nextnode = e
# e.nextnode = f

m = Node(8)
n = Node(9)
o = Node(7)
p = Node(25)
# q = Node(4)
# r = Node(5)
# s = Node(6)


m.nextnode = n
n.nextnode = o
o.nextnode = p
# p.nextnode = q
# q.nextnode = r
# r.nextnode = s

first_list = LinkedList()
first_list.head = a

second_list = LinkedList()
second_list.head = m


print "*** Ans ***\n"

def intersection(one_list,two_list):
    x=one_list.size()
    y= two_list.size()

    if x > y:
        first = x - y
        first_head = one_list.head
        while first_head is not None:
            first_head = first_head.nextnode
            first = first - 1
            if first == 0:
                break

        one_list.head = first_head

        while first_head is not None and second_list.head is not None:
            if first_head.data == second_list.head.data:
                return first_head.data
            else:
                first_head = first_head.nextnode
                second_list.head = second_list.head.nextnode

    if y > x:
        second = y - x
        second_head = two_list.head
        while second_head is not None:
            second_head = second_head.nextnode
            second = second - 1
            if second == 0:
                break

        two_list.head = second_head

        while second_head is not None and one_list.head is not None:
            if second_head.data == one_list.head.data:
                return second_head.data
            else:
                second_head = second_head.nextnode
                one_list.head = one_list.head.nextnode

    if x == y:
        while second_list.head is not None and one_list.head is not None:
            if second_list.head.data == one_list.head.data:
                return second_list.head.data
            else:
                second_list.head = second_list.head.nextnode
                one_list.head = one_list.head.nextnode

    return None

print intersection(first_list,second_list)