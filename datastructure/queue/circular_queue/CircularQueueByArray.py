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
        while current != self.__rear:
            print(self.__arr[current], end=" ")
            if current + 1 == self.__size:
                current = 0
            else:
                current += 1
        else:
            print(self.__arr[current], end="\n")

    def enqueue(self, value):

        if self.__front == -1:
            self.__front = 0
            self.__rear = 0
        else:

            if self.__rear + 1 == self.__size:
                if self.__front == 0:
                    raise Exception(f"Overflow! Defined size reached: {self.__size}")
                else:
                    self.__rear = 0
            elif self.__rear + 1 == self.__front:
                raise Exception(f"Overflow! Defined size reached: {self.__size}")
            else:
                self.__rear += 1

        self.__arr[self.__rear] = value

    def dequeue(self):

        if self.__front == -1:
            raise Exception(f"Underflow! Empty queue.")

        temp = self.__arr[self.__front]
        self.__arr[self.__front] = None

        if self.__front == self.__rear:
            self.__front = -1
            self.__rear = -1
        elif self.__front + 1 == self.__size and self.__rear < self.__front:
            self.__front = 0
        else:
            self.__front += 1

        return temp

