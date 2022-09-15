from Node import get_default
from Crud import read, add_values


def reverse(node):

    if node is None:
        return node

    prev = node
    curr = node.next
    prev.next = None

    while curr is not None:
        temp_next = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next

    return prev


if __name__ == "__main__":
    head = get_default()
    add_values(head, 5, 6, 7, 8, 9)
    read(head)

    head = reverse(head)
    read(head)
