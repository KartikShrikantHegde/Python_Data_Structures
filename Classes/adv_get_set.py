class Fruit():

    def __init__(self, **kwargs):
        self.variables = kwargs

    def description(self, Age):
        print "My Discription",self.variables

    def get_variable(self,k):
        return self.variables.get(k,None)

    def set_variable(self,k,v):
        self.variables[k] = v

# Creating objects

def main():
    lemon = Fruit(feet = 3, Age = 10)
    lemon.set_variable('taste','sour')
    print lemon.get_variable('feet')
    print lemon.get_variable('taste')
    lemon.description("Age")

if __name__ == "__main__":
    main()