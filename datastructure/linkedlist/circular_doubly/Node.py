class Node:

    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


def get_default():
    head = Node(0)

    node = Node(1)
    head.next = node
    node.prev = head

    node2 = Node(2)
    node.next = node2
    node2.prev = node

    node3 = Node(3)
    node2.next = node3
    node3.prev = node2

    node4 = Node(4)
    node3.next = node4
    node4.prev = node3

    node4.next = head
    head.prev = node4

    return head
