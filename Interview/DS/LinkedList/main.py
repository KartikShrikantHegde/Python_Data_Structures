__author__ = "Karthik"

import LinkedList

linkedList = LinkedList.LinkedList()

linkedList.insertStart('8')
linkedList.insertStart('4')
linkedList.insertStart('9')
linkedList.insertStart('7')
linkedList.insertStart('3')
linkedList.insertStart('7')
linkedList.insertStart('5')
linkedList.insertStart('3')
linkedList.insertStart('8')
linkedList.insertStart('6')
linkedList.insertStart('3')
linkedList.insertStart('5')
linkedList.insertStart('4')

# linkedList.rec_reverse()

# linkedList.fold()
# linkedList.traverseList()
linkedList.head = linkedList.reverse_k_list(linkedList.head,4)
# print linkedList.head.data

linkedList.traverseList()

# linkedList.remove('3')

# print linkedList.size()
# linkedList.traverseList()

# print linkedList.find('3')
