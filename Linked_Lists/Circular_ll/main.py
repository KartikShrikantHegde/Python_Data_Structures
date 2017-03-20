from LinkedList import LinkedList

cllist = LinkedList()

# Created linked list will be 11->2->56->12
cllist.insert(12)
cllist.insert(56)
cllist.insert(2)
cllist.insert(11)

print "Contents of circular Linked List"
cllist.traverse()