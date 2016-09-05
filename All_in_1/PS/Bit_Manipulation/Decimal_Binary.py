#  Import the already implemented stack

from Stacks.Stack_Implementation import Stack

def dec_binary(decNumber):
    
     # Initialize the stack
    myStack = Stack()

    while decNumber > 0:
        reminder = decNumber % 2
        myStack.push(reminder)
        
        #  the no is convered to floor value
        decNumber = decNumber // 2

    binString = ""
    while not myStack.isEmpty():
        binString = binString + str(myStack.pop())

    return binString

print(dec_binary(42))
