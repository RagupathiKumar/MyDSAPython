class Stack:

    def __init__(self, size):
        self.__top = -1
        self.__size = size
        self.__arr = [None] * size

    def push(self, value):

        if self.__top + 1 == self.__size:
            raise Exception(f"Stack Overflow! Defined size reached: {self.__size}")

        self.__top += 1
        self.__arr[self.__top] = value

    def pop(self):

        if self.__top == -1:
            raise Exception(f"Stack Underflow! Empty stack.")

        temp = self.__arr[self.__top]
        self.__arr[self.__top] = None
        self.__top -= 1
        return temp

    def peek(self):

        if self.__top == -1:
            raise Exception(f"Stack Underflow! Empty stack.")

        return self.__arr[self.__top]

    def show(self):

        for i in range(self.__top, -1, -1):
            print(self.__arr[i], end=" ")
        else:
            print("")
