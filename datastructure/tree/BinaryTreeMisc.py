from BinaryTree import Node

root = Node(6)
root.left = Node(4)
root.right = Node(7)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(9)
root.left.left.left = Node(1)


def height(node):
    if node is None:
        return 0

    l_height = height(node.left)
    r_height = height(node.right)
    if l_height > r_height:
        return l_height + 1
    else:
        return r_height + 1


def total_no_of_nodes(node):
    if node is None:
        return 0

    return total_no_of_nodes(node.left) \
        + total_no_of_nodes(node.right) \
        + 1


print(height(root))
print(total_no_of_nodes(root))
