class Example(object):
    def __init__(self,val):
        self.x = val

    def display(self):
        x = 30
        print x, self.x

temp = Example(10)
temp.display()
