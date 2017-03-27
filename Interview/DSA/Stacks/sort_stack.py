from Stacks.Stack_Implementation import Stack


s = Stack()
s.push(5)
s.push(3)
s.push(9)
s.push(2)
s.push(6)


def sortAscending(s):
    s1 = Stack()
    while not s.isEmpty():
        temp = s.pop()
        if s1.isEmpty() or temp > s.peek():
            s1.push(temp)
        else:
            while s1.peek() > temp:
                s.push(s1.pop())
                if s1.isEmpty():
                    break
            s1.push(temp)
    return s1

print sortAscending(s)