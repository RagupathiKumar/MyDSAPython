class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def get_default():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head
    return head
