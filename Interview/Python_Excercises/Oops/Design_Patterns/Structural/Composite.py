''' Challenge is to provide submethods inside methods like recursive tree data structure.
so goal is to build a menu like application '''


class Component(object):
    """ Abstract class """

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):
    """ Concrete class """

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        self.name = args[0]

    def component_function(self):
        print ("{}".format(self.name))


class Composite(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        self.name = args[0]

        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        print "{}".format(self.name)

        for i in self.children:
            i.component_function()


sub1 = Composite("submenu1")

sub11 = Child("sub_submenu1")

sub12 = Child("sub_submenu2")

sub1.append_child(sub11)

sub1.append_child(sub12)

top = Composite("top-menu")

sub2 = Child("submenu2")

top.append_child(sub1)

top.append_child(sub2)

top.component_function()
