
from Balanced_Trees.Binary_Search_Trees.Node import Node
from Stacks.Stack_Implementation import Stack
root = Node(1)
root.leftChild = Node(2)
root.rightChild = Node(3)
root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.leftChild.leftChild.leftChild = Node(8)
root.leftChild.rightChild.leftChild = Node(9)
root.rightChild.leftChild = Node(6)
root.rightChild.rightChild = Node(7)
root.rightChild.rightChild.rightChild = Node(10)



def zizag(root):
    if root is None:
        return

    my_stack1 = Stack()
    my_stack1.push(root)
    my_stack2 = Stack()

    while not my_stack1.isEmpty() or not my_stack2.isEmpty():
        while not my_stack1.isEmpty():
            root = my_stack1.pop()
            print root.data
            if root.leftChild is not None:
                my_stack2.push(root.leftChild)
            if root.rightChild is not None:
                my_stack2.push(root.rightChild)

        while not my_stack2.isEmpty():
            root = my_stack2.pop()
            print root.data
            if root.rightChild is not None:
                my_stack1.push(root.rightChild)
            if root.leftChild is not None:
                my_stack1.push(root.leftChild)


zizag(root)


