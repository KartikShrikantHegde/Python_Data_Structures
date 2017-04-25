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
