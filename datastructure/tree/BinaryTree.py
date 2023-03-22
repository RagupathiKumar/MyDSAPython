class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):  # this method is more applicable to binary search tree
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

    def insert(self, val):
        new_node = Node(val)

        if self.root is None:
            self.root = new_node
            return

        q = [self.root]

        while len(q) > 0:
            node = q.pop(0)

            if node.left is None:
                node.left = new_node
                break
            else:
                q.append(node.left)

            if node.right is None:
                node.right = new_node
                break
            else:
                q.append(node.right)

    def traversal(self, traversal_type="PRE"):
        if traversal_type == "PRE":
            self.__pre_order_traversal(self.root)
        elif traversal_type == "IN":
            self.__in_order_traversal(self.root)
        elif traversal_type == "POST":
            self.__post_order_traversal(self.root)
        print("")

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





