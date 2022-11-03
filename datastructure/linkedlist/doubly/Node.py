class Node:

    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


def get_default():

    head = Node(1)

    node2 = Node(2)
    node2.prev = head
    head.next = node2

    node3 = Node(3)
    node3.prev = node2
    node2.next = node3

    node4 = Node(4)
    node4.prev = node3
    node3.next = node4

    return head
