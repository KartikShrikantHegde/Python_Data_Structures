A function such as len() will
exploit the __len__() special method of a class.
What this means is that we have a tidy, universal public interface ( len(x) ) that
works on any kind of class. Python's polymorphism is based in part on the way any
class can implement a __len__() method; objects of any such class will respond to
the len() function.