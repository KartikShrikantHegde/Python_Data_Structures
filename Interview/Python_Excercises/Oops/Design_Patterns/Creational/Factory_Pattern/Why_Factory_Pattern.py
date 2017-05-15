''' Factory pattern is an object for the creation of other objects
In this example get_pet method is the factory method tha produces objects of diff class'''

''' Why Factory pattern ?

1. The client just asks for object but without knowing who is producing it (factory method is producing it)

2. Factory method is used just for object creation

3. . The idea behind a factory is to simplify an object creation. It is easier to track which objects are created
     if this is done through a central function,
     in contrast to letting a client create objects using a direct class instantiation.

4. A factory reduces the complexity of maintaining an application by decoupling the code that creates an object from the code that uses it

There are 2 types.

Factory method and abstract factory

'''