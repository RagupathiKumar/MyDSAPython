from CircularQueueByArray import Queue

q = Queue(5)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.show()

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.show()

q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.show()

print(q.dequeue())
print(q.dequeue())
q.show()


print(q.dequeue())
print(q.dequeue())