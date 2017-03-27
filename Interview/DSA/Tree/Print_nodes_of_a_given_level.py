
from Balanced_Trees.Binary_Search_Trees.Node import Node
from Stacks.Stack_Implementation import Stack
from Queue import Queue

root = Node(10)
root.leftChild = Node(20)
root.rightChild = Node(30)
root.leftChild.leftChild = Node(40)
root.leftChild.rightChild = Node(50)
root.rightChild.leftChild = Node(60)
root.rightChild.rightChild = Node(70)


def reverse_level_order(root, my_level):
    if root is None:
        return None

    if my_level == 1:
        return root.data

    my_queue1 = Queue()
    my_queue2 = Queue()
    my_queue1.put(root)
    counter = 1

    while not my_queue1.empty() or not my_queue2.empty():
        while not my_queue1.empty():
            if counter == my_level:
                while not my_queue1.empty():
                    print my_queue1.get().data
                break

            root = my_queue1.get()

            if root.leftChild:
                my_queue2.put(root.leftChild)

            if root.rightChild:
                my_queue2.put(root.rightChild)

        counter += 1

        while not my_queue2.empty():
            if counter == my_level:
                while not my_queue2.empty():
                    print my_queue2.get().data
                break
            root = my_queue2.get()

            if root.leftChild:
                my_queue1.put(root.leftChild)

            if root.rightChild:
                my_queue1.put(root.rightChild)

        counter += 1

reverse_level_order(root,5)