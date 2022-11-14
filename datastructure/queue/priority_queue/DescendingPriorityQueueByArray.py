class Item:

    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:

    def __init__(self, size):
        self.__size = size
        self.__arr = [None] * size
        self.__index = -1

    def enqueue(self, value, priority):
        item = Item(value, priority)

        if self.__index + 1 == self.__size:
            raise Exception(f"Overflow! Queue is full : {self.__size}")

        self.__index += 1
        self.__arr[self.__index] = item

    def peek(self):

        if self.__index == -1:
            raise Exception(f"Underflow! Queue is empty.")

        highest_priority = -1
        highest_priority_index = -1

        for index in range(len(self.__arr)):
            item = self.__arr[index]

            if item is None:
                continue

            if item.priority > highest_priority:
                highest_priority = item.priority
                highest_priority_index = index
            elif item.priority == highest_priority \
                    and highest_priority_index > -1 \
                    and self.__arr[index].value > self.__arr[highest_priority_index].value:
                highest_priority = item.priority
                highest_priority_index = index

        return highest_priority_index

    def dequeue(self):

        highest_priority_index = self.peek()
        temp = self.__arr[highest_priority_index]

        index = highest_priority_index
        while index < len(self.__arr) - 1:
            self.__arr[index] = self.__arr[index + 1]
            index += 1
        else:
            self.__arr[index] = None

        self.__index -= 1
        return temp

    def show(self):
        for item in self.__arr:
            if item is not None:
                print(item.value, end=" ")
        print("")
