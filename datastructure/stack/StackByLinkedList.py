class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    __head = None

    def push(self, value):
        node = Node(value)
        node.next = self.__head
        self.__head = node

    def pop(self):

        if self.__head is None:
            raise Exception(f"Stack Underflow! Empty stack.")

        first = self.__head
        self.__head = self.__head.next
        return first.value

    def peek(self):

        if self.__head is None:
            raise Exception(f"Stack Underflow! Empty stack.")

        return self.__head.value

    def show(self):

        node = self.__head
        while node is not None:
            print(node.value, end=" ")
            node = node.next
        else:
            print("")
