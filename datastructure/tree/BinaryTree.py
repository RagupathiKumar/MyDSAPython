class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)

        if self.root is None:
            self.root = node
        else:
            current = self.root

            while True:
                parent = current

                if val < parent.value:
                    current = parent.left
                    if current is None:
                        parent.left = node
                        break
                else:
                    current = parent.right
                    if current is None:
                        parent.right = node
                        break

    def traversal(self):
        self.__pre_order_traversal(self.root)
        print("")
        self.__in_order_traversal(self.root)
        print("")
        self.__post_order_traversal(self.root)

    def __pre_order_traversal(self, current):
        if current is not None:
            print(current.value, end=" ")
            self.__pre_order_traversal(current.left)
            self.__pre_order_traversal(current.right)

    def __in_order_traversal(self, current):
        if current is not None:
            self.__in_order_traversal(current.left)
            print(current.value, end=" ")
            self.__in_order_traversal(current.right)

    def __post_order_traversal(self, current):
        if current is not None:
            self.__post_order_traversal(current.left)
            self.__post_order_traversal(current.right)
            print(current.value, end=" ")





