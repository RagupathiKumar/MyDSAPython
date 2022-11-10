# from QueueByArray import Queue
from QueueByLinkedList import Queue

# q = Queue(5)
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.show()

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

q.show()
