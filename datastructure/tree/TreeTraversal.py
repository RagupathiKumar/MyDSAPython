from BinaryTree import Node

root = Node(6)
root.left = Node(4)
root.right = Node(7)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(9)


def pre_order(node):
    if node is None:
        return

    print(node.value, end=" ")
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if node is None:
        return

    in_order(node.left)
    print(node.value, end=" ")
    in_order(node.right)


def post_order(node):
    if node is None:
        return

    post_order(node.left)
    post_order(node.right)
    print(node.value, end=" ")


if __name__ == '__main__':
    pre_order(root)
    print("")
    in_order(root)
    print("")
    post_order(root)
