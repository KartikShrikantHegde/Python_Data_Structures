# from Linked_Lists.single_ll.Node import Node
from Linked_Lists.Single_ll.LinkedList import LinkedList

class Node(object):
    def __init__(self,val):
        self.data = val
        self.nextnode = None



class SortList(object):
    def sortlist(self,my_arr):


        my_list = LinkedList()

        self.head = Node(my_arr[0])
        my_list.head = self.head
        current = self.head

        for i in range(1,len(my_arr)):
            my_arr[i] = Node(my_arr[i])
            # thisnode = Node(my_arr[i])
            current.nextnode = my_arr[i]
            current = my_arr[i]

        print my_list.traverseList()


my_arr = [1]
my_obj = SortList()
my_obj.sortlist(my_arr)


