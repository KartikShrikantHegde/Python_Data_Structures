from Queues.Implementation import Queue


class NewNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = NewNode(5)
b = NewNode(3)
c = NewNode(8)
d = NewNode(2)
e = NewNode(4)
f = NewNode(1)
g = NewNode(7)
h = NewNode(6)
i = NewNode(9)
j = NewNode(10)
k = NewNode(11)

a.left = b
a.right = c
b.left = d
b.right = e
d.left = f
c.right = i
c.left = g
g.left = h
i.right = j
j.right = k


def level_order_link_list(root):
    if root is None:
        return None

    my_queue = Queue()
    my_queue.add(root)
    my_list = []
    prev = 1
    next = 0
    temp_list = []
    while not my_queue.isEmpty():
        root = my_queue.remove()
        temp_list.append(root.val)
        if root.left:
            my_queue.add(root.left)
            next += 1
        if root.right:
            my_queue.add(root.right)
            next += 1

        prev -= 1
        if prev == 0:
            my_list.append(temp_list)
            prev = next
            next = 0
            temp_list = []
        else:
            continue

    return my_list


print level_order_link_list(a)
