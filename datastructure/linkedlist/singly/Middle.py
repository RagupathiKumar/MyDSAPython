from Node import get_default
from Crud import read, add_values


def get_mid(head_node):
    if head_node is None or \
            head_node.next is None:
        return head_node

    slow_pointer = head_node
    fast_pointer = head_node

    while fast_pointer.next is not None and \
            fast_pointer.next.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    return slow_pointer


if __name__ == '__main__':
    head = get_default()
    add_values(head, 4, 5, 6, 7, 8)
    read(head)

    print(get_mid(head).value)

    add_values(head, 9)
    read(head)

    print(get_mid(head).value)
