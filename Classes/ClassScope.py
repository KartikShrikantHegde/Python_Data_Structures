class Animal(object):
    """Makes cute animals."""
    is_alive = True                                     # this is a member variable
    def __init__(self, name, age):                      # Instance Variable
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive