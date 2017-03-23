from Stacks.Stack_Implementation import Stack

my_stack1 = Stack()
my_stack2 = Stack()


def add_item(item):
    my_stack1.push(item)


def remove_item():
    if my_stack2.isEmpty():
        while not my_stack1.isEmpty():
            my_stack2.push(my_stack1.pop())
    while not my_stack2.isEmpty():
        print my_stack2.pop()


class Solution(object):
    pass

my_object = Solution()
add_item('a')
add_item('b')
add_item('c')
add_item('d')
add_item('e')

remove_item()
