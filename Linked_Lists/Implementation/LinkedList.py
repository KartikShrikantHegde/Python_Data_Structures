
import Node
class LinkedList(object):

    def __init__(self):
        self.head = None

    def insertStart(self,data):

        newNode = Node.Node(data)

        if not self.head :
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size(self):

        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode

        return size


    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:
            print("%s " % actualNode.data)
            actualNode = actualNode.nextNode

    def insertEnd(self,data):

        newNode = Node.Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def remove(self,data):
        if( self.head ):
            if( data == self.head.data ):
                self.head = self.head.nextNode
            else:
                self.head.remove(data,self.head)





