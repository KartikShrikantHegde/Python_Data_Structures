
class Node(object):

    def __init__(self,data):
        self.data=data
        self.nextNode = None


a = Node (1)
b = Node (2)
c = Node (10)

print a.data
print b.data
print c.data

a.nextNode = b
b.nextNode = c

print a.nextNode.data
print b.nextNode.data


