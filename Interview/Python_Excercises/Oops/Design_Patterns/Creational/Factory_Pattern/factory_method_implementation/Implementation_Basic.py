# Factory Method, we execute a single function, passing a parameter that provides
# information about what we want. We are not required to know any details about how the object is
# implemented and where it is coming from.




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

    pets = dict(dog=Dog("Danny"), cat=Cat("Rossy"))

    return pets[pet]


d = get_pet("dog")
c = get_pet("cat")

print d.speak()
print c.speak()
