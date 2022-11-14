class Node:

    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None


class PriorityQueue:

    def __init__(self):
        self.__head = None
        self.__end = None

    def enqueue(self, value, priority):

        node = Node(value, priority)

        if self.__head is None:
            self.__head = node
            self.__end = node
            return

        previous = None
        current = self.__head
        while current is not None:

            if current.priority < node.priority:
                previous = current
                current = current.next
            elif current.priority == node.priority and current.value < node.value:
                previous = current
                current = current.next
            else:
                break

        if previous is None:
            node.next = self.__head
            self.__head = node
        elif current is None:
            self.__end.next = node
            self.__end = node
        else:
            previous.next = node
            node.next = current

    def peek(self):

        if self.__head is None:
            raise Exception(f"Underflow! Queue is empty.")

        return self.__head.value

    def dequeue(self):
        if self.__head is None:
            raise Exception(f"Underflow! Queue is empty.")

        temp = self.__head
        self.__head = self.__head.next
        return temp

    def show(self):
        current = self.__head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print("")
