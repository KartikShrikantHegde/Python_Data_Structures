'''
If interface is not compatible between a client and a server, adapter provides a
alternative conversion by providing a alternative interface
so note that here our specific methods have speak method where as
 clint just calls the speak method in general
 '''

class Korean(object):
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An - neyong"

class British(object):
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello!"

class Adapter(object):
    ''' Change the methods to '''

    def __init__(self,object,**adapted_method):
        self._object = object
        self.__dict__.update(adapted_method)


    def __getattr__(self, attr):
        return getattr(self._object,attr)

objects = []

korean = Korean()

british = British()

objects.append(Adapter(korean,speak = korean.speak_korean))
objects.append(Adapter(british,speak = british.speak_english))

for obj in objects:
    print "{} says '{}'\n".format(obj.name,obj.speak())

