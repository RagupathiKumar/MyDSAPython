from DoubleEndedQueue import Queue

q = Queue(5)

q.enqueue_rear(1)
q.enqueue_rear(2)
q.enqueue_rear(3)
q.enqueue_rear(4)
q.enqueue_rear(5)
q.show()

print(q.dequeue_front())
print(q.dequeue_front())
print(q.dequeue_rear())  # this is rear dequeue -- keep an eye
q.show()

q.enqueue_front(6)
q.enqueue_front(7)
q.show()

print(q.dequeue_front())
print(q.dequeue_rear())  # this is rear dequeue -- keep an eye
print(q.dequeue_front())
q.show()