class MinStack:
    def __init__(self):
        self.q = []

    def push(self, x):
        curMin = self.getMin()
        if curMin is None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    # @return nothing
    def pop(self):
        return self.q.pop()

    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]


my_stack = MinStack()
my_stack.push(-2)
my_stack.push(0)
my_stack.push(-3)
print my_stack.getMin()
print my_stack.pop()
print my_stack.top()
print my_stack.getMin()

