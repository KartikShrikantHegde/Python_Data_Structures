
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


def print_reverse_level_order(root):
    if root is None:
        return None

    my_stack = Stack()
    my_queue1 = Queue()
    my_queue2 = Queue()
    my_queue1.put(root)

    while not my_queue1.empty() or not my_queue2.empty():
        while not my_queue1.empty():
            root = my_queue1.get()

            if root.rightChild:
                my_queue2.put(root.rightChild)

            if root.leftChild:
                my_queue2.put(root.leftChild)

            my_stack.push(root)


        while not my_queue2.empty():
            root = my_queue2.get()

            if root.rightChild:
                my_queue1.put(root.rightChild)

            if root.leftChild:
                my_queue1.put(root.leftChild)

            my_stack.push(root)

    while not my_stack.isEmpty():
        print my_stack.pop().data


print_reverse_level_order(root)