class Stack:

    def __init__(self, size):
        self.top = -1
        self.size = size
        self.arr = [None] * size

    def push(self, value):

        if self.top + 1 == self.size:
            raise Exception(f"Stack Overflow! Defined size reached: {self.size}")

        self.top += 1
        self.arr[self.top] = value

    def pop(self):

        if self.top == -1:
            raise Exception(f"Stack Underflow! Empty stack.")

        temp = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return temp

    def peek(self):

        if self.top == -1:
            raise Exception(f"Stack Underflow! Empty stack.")

        return self.arr[self.top]

    def show(self):

        for i in range(self.top, -1, -1):
            print(self.arr[i], end=" ")
        else:
            print("")
