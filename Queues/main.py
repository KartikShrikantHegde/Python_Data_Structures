import Implementation

q = Implementation.Queue()

print q.isEmpty()

q.add(4)
q.add('dog')
q.add("Man")

print q.remove()
print q.peek()
print q.remove()
