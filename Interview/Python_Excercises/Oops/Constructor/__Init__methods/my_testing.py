class Sample(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y


class ChildSample(Sample):
    def sample(self):
        return self.x, self.y


my_child = ChildSample(10,20)
print my_child.sample()