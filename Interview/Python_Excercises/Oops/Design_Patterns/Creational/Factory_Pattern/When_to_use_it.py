# If you realize that you cannot track the objects created by your application
# because the code that creates them is in many different places instead of a single function/method,
# you should consider using the Factory Method pattern [Eckel08, page 187].
# The Factory Method centralizes an object creation and tracking your objects becomes much easier.


# Note that it is absolutely fine to create more than one Factory Method, and
# this is how it is typically done in practice.
# Each Factory Method logically groups the creation of objects that have similarities.
# For example, one Factory Method might be responsible for connecting you to
# different databases (MySQL, SQLite), another Factory Method might be responsible
# for creating the geometrical object that you request (circle, triangle), and so on.

'''
The Factory Method is also useful when you want to decouple an object creation
from an object usage. We are not coupled/bound to a specific class when creating an object,
we just provide partial information about what we want by calling a function. This means that introducing
changes to the function is easy without requiring any changes to the code that uses it


Another use case worth mentioning is related to improving the
performance and memory usage of an application. A Factory Method can improve the
performance and memory usage by creating new objects only if it is absolutely necessary
 When we create objects using a direct class instantiation, extra memory is allocated every time
a new object is created (unless the class uses caching internally, which is usually not the case)
'''