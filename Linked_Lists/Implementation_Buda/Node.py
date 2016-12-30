__author__ = "Karthik"

class Node(object):
    
    def __init__(self,data):
        self.data=data
        self.nextnode = None

    def remove(self, data, previousNode):
        if self.data == data:
            previousNode.nextnode = self.nextnode
            del self.data
        else:
            if self.nextnode is not None:
                self.nextnode.remove(data,self)

    
    