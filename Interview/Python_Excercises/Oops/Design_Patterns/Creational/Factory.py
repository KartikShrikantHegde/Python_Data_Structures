''' Factory pattern is an object for the creation of other objects
In this example get_pet method is the factory method tha produces objects of diff class'''


class Dog(object):
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat(object):
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def get_pet(pet):

    """ Factory method """

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]


d = get_pet("dog")
c = get_pet("cat")

print d.speak()
print c.speak()
