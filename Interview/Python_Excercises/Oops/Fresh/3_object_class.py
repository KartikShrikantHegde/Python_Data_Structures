# Object is superclass of all the classes.
#
# Each Python class definition has an implicit superclass: object . It's a very
# simple class definition that does almost nothing. We can create instances of object ,
# but we can't do much with them because many of the special methods simply
# raise exceptions.
#

class X:
    pass

print X.__class__.__base__