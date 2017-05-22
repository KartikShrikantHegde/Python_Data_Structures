''' Helps to solve the problem where we need to create many identical objects individually.
'''

import copy

class Prototype(object):
    def __init__(self):
        self._objects = {}

    def register_object(self,name,obj):
        ''' Register an object '''
        self._objects[name] = obj


    def unregister_object(self, name):
        ''' UnRegister an object '''
        del self._objects[name]

    def clone(self,name,**attr):
        ''' clone an object and update its attributes '''

        ''' Use the deepcopy to create a seperate copy of the object from dict'''
        obj = copy.deepcopy(self._objects.get(name))

        ''' if you want to update the object attribute you are cloning '''

        obj.__dict__.update(attr)
        return obj


class Car(object):
    def __init__(self):
        self.name = "Ferrari"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_object('my_obj1',c)
c1 = prototype.clone('my_obj1')
print c1