class Animal(object):
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!

    def description(self):
        print self.name
        print self.age

Lion = Animal("Daam",22)
Lion.description()