there could be times when we
needn't set all of the attributes in the __init__() method.

class Rectangle:
    def area( self ):
        return self.length * self.width

The Rectangle class has a method that uses two attributes to return a value.
The attributes have not been initialized anywhere. This is legal Python. It's a
little strange to avoid specifically setting attributes, but it's valid.
The following is an interaction with the Rectangle class:

>>> r= Rectangle()
>>> r.length, r.width = 13, 8
>>> r.area()
104