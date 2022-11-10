class Queue:

    def __init__(self, size):
        self.__front = -1
        self.__rear = -1
        self.__size = size
        self.__arr = [None] * size

    def show(self):

        for num in self.__arr:
            print(num, end=" ")
        else:
            print("")

    def enqueue(self, value):

        if self.__rear + 1 > self.__size:
            raise Exception(f"Overflow! Defined size reached: {self.__size}")

        if self.__front == -1:
            self.__front += 1
            self.__rear += 1
        else:
            self.__rear += 1

        self.__arr[self.__rear] = value

    def dequeue(self):

        if self.__front == -1:
            raise Exception(f"Underflow! Empty queue.")

        temp = self.__arr[self.__front]
        self.__arr[self.__front] = None

        if self.__front + 1 > self.__rear:
            self.__front = -1
            self.__rear = -1
        else:
            self.__front += 1

        return temp
