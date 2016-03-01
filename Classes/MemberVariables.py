class Animal(object):

    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!

    def description(self):
        print self.name
        print self.age

hippo = Animal ("S",33)
hippo.description()

sloth = Animal("f",44)

ocelot = Animal ("l",12)

print hippo.health

print sloth.health
sloth.health ="bad"
print sloth.health
print ocelot.health