class Example(object):
    counter = 0
    my_str = "Hello"
    def __init__(self,val):
        self.val = val
        Example.counter = Example.counter + 1


    def display(self):

        # can access both static and instance variable
        print self.val
        print Example.my_str

        # call static method as well
        Example.my_method()

    @staticmethod
    def show():
        pass

    @staticmethod
    def my_method():

        # CANT ACCESS INSTANCE VARIABLE AND METHODS
        # print val
        # display()


        # Access only static method and static variable inside static block

        print Example.my_str
        Example.show()


        print Example.display()

temp = Example('temp')
proxy = Example('proxy')

temp.display()