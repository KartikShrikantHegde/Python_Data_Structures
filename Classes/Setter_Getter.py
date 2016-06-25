class Fruit(object):

    def __init__(self, color = "Red"):
        self._color = color

    def description(self):
        print "My Discription",self

    def get_color(self):
        return self._color

    def set_color(self,color):
        self._color = color

# Creating objects

def main():
    lemon = Fruit()
    print lemon.get_color()
    lemon.set_color("Blue")
    print lemon.get_color()

if __name__ == "__main__":
    main()