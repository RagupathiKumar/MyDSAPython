class Queue:

    def __init__(self, size):
        self.__front = -1
        self.__rear = -1
        self.__size = size
        self.__arr = [None] * size

    def show(self):

        if self.__front == -1:
            return

        current = self.__front
        while current <= self.__rear:
            print(self.__arr[current], end=" ")
            current += 1
        else:
            print("")

    def enqueue_front(self, value):

        if self.__front == 0:
            raise Exception(f"Enqueue front cannot be allowed : {self.__front}")

        if self.__front == -1:
            self.__front = 0
            self.__rear = 0
        else:
            self.__front -= 1

        self.__arr[self.__front] = value

    def enqueue_rear(self, value):

        if self.__rear + 1 == self.__size:
            raise Exception(f"Overflow! Defined size reached: {self.__size}")

        if self.__front == -1:
            self.__front = 0
            self.__rear = 0
        else:
            self.__rear += 1

        self.__arr[self.__rear] = value

    def dequeue_front(self):

        if self.__front == -1:
            raise Exception(f"Underflow! Empty queue.")

        temp = self.__arr[self.__front]
        self.__arr[self.__front] = None

        if self.__front == self.__rear:
            self.__front = -1
            self.__rear = -1
        else:
            self.__front += 1

        return temp

    def dequeue_rear(self):

        if self.__rear == -1:
            raise Exception(f"Underflow! Empty queue.")

        temp = self.__arr[self.__rear]
        self.__arr[self.__rear] = None

        if self.__front == self.__rear:
            self.__front = -1
            self.__rear = -1
        else:
            self.__rear -= 1

        return temp
