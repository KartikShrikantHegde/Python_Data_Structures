from Linked_Lists.Single_ll.Node import Node
from Linked_Lists.Single_ll.LinkedList import LinkedList

a = Node(5)
b = Node(4)
c = Node(1)

a.nextnode = b
b.nextnode = c

my_list = LinkedList()
my_list.head = a

# for i in range(1, len(my_arr)):
#     current_val = my_arr[i]
#     position = i
#
#     while position > 0 and my_arr[position - 1] > current_val:
#         my_arr[position] = my_arr[position - 1]
#         position -= 1
#
#     my_arr[position] = current_val



class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        current_node = head.nextnode
        prev_node = head
        position = 0
        counter = 0
        while current_node:
            current_val = current_node.data
            position += 1

            while position > 0 and prev_node.data > current_val:
                current_node.data = prev_node.data
                prev_node = current_node
                current_node = current_node.nextnode
                position -= 1

            counter += 1
            position = counter

        return prev_node


my_list.traverseList()
my_obj = Solution()
my_obj.insertionSortList(a)
my_list.traverseList()