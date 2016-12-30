__author__ = "Karthik"

import LinkedList

linkedList = LinkedList.LinkedList()

linkedList.insertStart('c')
linkedList.insertStart('b')
linkedList.insertStart('a')
linkedList.insertEnd('1')
linkedList.insertEnd('2')
linkedList.insertEnd('3')

linkedList.traverseList()

linkedList.remove('3')

print linkedList.size()
linkedList.traverseList()

print linkedList.find('3')
