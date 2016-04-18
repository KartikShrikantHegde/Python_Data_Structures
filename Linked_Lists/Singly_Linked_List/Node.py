class Node(object):
    def __init__(self,data,next = None):
        self.data = data
        self.nextnode = next

    def get_next(self):
        return self.nextnode

    def set_next(self,next):
        self.nextnode = next

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data = data







