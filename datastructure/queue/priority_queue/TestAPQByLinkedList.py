from AscendingPriorityQueueByLinkedList import PriorityQueue


q = PriorityQueue()  # 33 66 44 22 11
q.enqueue(11, 5)
q.enqueue(22, 4)
q.enqueue(44, 2)
q.enqueue(66, 1)
q.enqueue(33, 1)
q.show()

print(q.peek())

print(q.dequeue().value)
q.show()

print(q.dequeue().value)
q.show()

print(q.dequeue().value)
q.show()

print(q.dequeue().value)
q.show()

print(q.dequeue().value)
