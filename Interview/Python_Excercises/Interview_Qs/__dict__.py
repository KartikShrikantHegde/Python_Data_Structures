Basically it contains all the attributes which describe the object under question.
It can be used to alter or read the attributes.

A dictionary or other mapping object used to store an object’s (writable) attributes.
Remember, everything is an object in python. When I say everything, I mean everything like functions, classes, objects etc (Ya you read it right, classes. Classes are also objects). For example,

def func():
    pass
func.temp = 1

print func.__dict__

class TempClass(object):
    a = 1
    def tempFunction(self):
        pass

print TempClass.__dict__
Output

{'temp': 1}
{'a': 1, '__module__': '__main__', 'tempFunction': <function tempFunction at 0x7f