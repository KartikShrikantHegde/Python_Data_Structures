from Balanced_Trees.Binary_Search_Trees.Node import Node


class MinBst(object):

    def create_min_bst(self, array):
        if array is None:
            return
        return self._create_min_bst(array, 0, len(array) - 1)

    def _create_min_bst(self, array, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        node = Node(array[mid])
        node.left = self._create_min_bst(array, start, mid - 1)
        node.right = self._create_min_bst(array, mid + 1, end)
        return node

    def traverseInOrder(self,root):
        if root:
            self.traverseInOrder(root.left)
            print root.data
            self.traverseInOrder(root.right)


my_arr = [0,1,2,3,4,5,6]
my_obj = MinBst()
a = my_obj.create_min_bst(my_arr)
my_obj.traverseInOrder(a)

# print new_node.traverseInOrder()


