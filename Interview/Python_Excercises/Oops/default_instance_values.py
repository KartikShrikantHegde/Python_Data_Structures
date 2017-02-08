class Example(object):
    def __init__(self,val = None):
        self.x = val

#OR
# class Example(object):
#     def __init__(self):
#         self.x = None

#OR
# class Example(object):
#     def __init__(self):
#         self.x = 10
#         self.y = 20


temp = Example()
print temp.x
