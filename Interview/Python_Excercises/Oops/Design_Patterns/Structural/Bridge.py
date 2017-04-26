''' Provides solutions to two unrelated parallel abstractions
1. one is implementation specific
2. Other is implementation independent

Solution is to seperate abstractions into 2 diff hierarchies'''

class APIOne(object):
    def draw_circle(self,x,y,radius):
        print "Drawing 1 at {}{} of {}".format(x,y,radius)

class APItwo(object):
    def draw_circle(self, x, y, radius):
        print "Drawing 2 at {}{} of {}".format(x, y, radius)


# Implementation independent

class Circle(object):
    def __init__(self,x,y,radius,drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x,self._y,self._radius)


circle1 = Circle(1,2,3,APIOne())
circle1.draw()

circle2 = Circle(2,5,6,APItwo())
circle2.draw()
