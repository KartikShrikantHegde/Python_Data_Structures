class Node(object):
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.nextnode = None

    def get_next(self):
        return self.nextnode

    def set_next(self,next):
        self.nextnode = next

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev = prev

    def get_data(self):
        return self.val

    def set_val(self,val):
        self.val = val

    