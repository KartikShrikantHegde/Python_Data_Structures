__author__= "Karthik Hegde"

''' Self is an first parameter to the method that takes place of the object we want to use
    __init__  -- Constructor in Python (init.py is module to tell submodules are python files)
    In Constructor, self is the first parameter always which takes the object being created.
    other parameters are the attributes of object passed as parameter from object.
    in self.name, self.color are the local variables which can be used anywhere else in other methods.

'''

class Fruit(object):

    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

# Creating objects

def main():
    lemon = Fruit("lemon", "yellow", "sour", False)
    lemon.description()
    lemon.is_edible()

if __name__ == "__main__":
    main()


'''
When your script is run by passing it as a command to the Python interpreter,

python myscript.py
all of the code that is at indentation level 0 gets executed. Functions and classes that are defined are, well, defined, but none of their code gets ran. Unlike other languages, there's no main() function that gets run automatically - the main() function is implicitly all the code at the top level.

In this case, the top-level code is an if block.  __name__ is a built-in variable which evaluate to the name of the current module. However, if a module is being run directly (as in myscript.py above), then __name__ instead is set to the string "__main__". Thus, you can test whether your script is being run directly or being imported by something else by testing

if __name__ == "__main__":
    ...
If that code is being imported into another module, the various function and class definitions will be imported, but the main() code won't get run. As a basic example, consider the following two scripts:

# file one.py
def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")

# file two.py
import one

print("top-level in two.py")
one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")
Now, if you invoke the interpreter as

python one.py
The output will be

top-level in one.py
one.py is being run directly
If you run two.py instead:

python two.py
You get

top-level in one.py
one.py is being imported into another module
top-level in two.py
func() in one.py
two.py is being run directly
Thus, when module one gets loaded, its __name__ equals "one" instead of __main__.

if __name__ == "__main__":
    main()

'''