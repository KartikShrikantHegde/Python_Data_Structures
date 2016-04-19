import Implementation

q=Implementation.Queue()


print q.isEmpty()

q.enqueue(4)
q.enqueue('dog')
q.enqueue("Man")

print q.dequeue()
print q.peek()
print q.dequeue()