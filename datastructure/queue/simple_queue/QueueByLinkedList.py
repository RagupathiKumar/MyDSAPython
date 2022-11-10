class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.__front = None
        self.__rear = None

    def show(self):

        node = self.__front
        while node is not None:
            print(node.value, end=" ")
            node = node.next
        else:
            print("")

    def enqueue(self, value):
        node = Node(value)

        if self.__front is None:
            self.__front = node
            self.__rear = node
        else:
            self.__rear.next = node
            self.__rear = self.__rear.next

    def dequeue(self):

        if self.__front is None:
            raise Exception(f"Queue Underflow! Empty queue.")

        node = self.__front

        if self.__front == self.__rear:
            self.__front = None
            self.__rear = None
        else:
            self.__front = self.__front.next

        return node.value

